from . import app, clarifai_api, ETSY_API_KEY
from flask import render_template, request, session, redirect, url_for
from instagram.client import InstagramAPI
import requests
from instagram import client
import operator

user_tags = {}

CONFIG = {
    'client_id': '5d99f0fac1084de5a71f889452248123',
    'client_secret': 'aba8aa200eaf417ca9ef54a9b83eddfd',
    'redirect_uri': 'https://172e3628.ngrok.com/insta-auth'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)


def get_tags_for_photo(photo_url):
    """
    Returns a list of all the tags for a photo using clarifai's
    image recognition.
    """
    result = clarifai_api.tag_image_urls(photo_url)
    tag_list = result['results'][0]['result']['tag']['classes']
    return tag_list


def get_common_tags(photos):
    """
    Return a list of top five tags among liked photos by user
    """
    rough = []
    master = {}

    for each in photos:
        rough.extend(tag5(get_tags_for_photo(each)))

    master[rough[0]] = 0

    for element in rough:
        if not element in master:
            master[element] = 1
        else:
            master[element] += 1

    sorted_master = tag5(
        sorted(master.iteritems(), key=operator.itemgetter(1), reverse=True))
    final = [keyword[0] for keyword in sorted_master]
    return final


def tag5(long):
    short = [long[i] for i in (0, 1, 2, 3, 4)]
    return short


def get_etsy_products(tags):
    """
    Returns a list of all the matching items currently on sale at Etsy
    """
    payload = {'api_key': ETSY_API_KEY, 'keywords': tags}
    res = requests.get(
        'https://openapi.etsy.com/v2/listings/active', params=payload)
    t = [{'listing_id': item['listing_id'], 'url': item['url']}
         for item in res.json()['results']]
    print t[0]['listing_id']
    # return [i['listing_id'] for i in res.json()['results']]
    return t


def get_listing_image(listing_id):
    try:
        payload = {'api_key': ETSY_API_KEY}
        res = requests.get(
            'https://openapi.etsy.com/v2/listings/%i/images' % listing_id, params=payload)
        return res.json()['results'][0]['url_fullxfull']
    except Exception as e:
        print e


def get_all_images(rec):
    all_images = []
    for each in rec:
        img = get_listing_image(each['listing_id'])
        image_details = {}
        all_images.append(img)
    return all_images


@app.route('/')
def index():
    url = unauthenticated_api.get_authorize_url(
        scope=["likes", "comments"])
    # return '<a href="%s">Connect with Instagram</a>' % url
    return render_template('index.html', url=url)


@app.route('/insta-auth')
def insta_auth():
    """
    Instagram Redirect URI endpoint
    """
    code = request.args.get("code")
    if not code:
        return render_template('error.html', error="Missing code in request args")
    try:
        access_token, user_info = unauthenticated_api.exchange_code_for_access_token(
            code)
        if not access_token:
            return 'Could not get access token'
        api = client.InstagramAPI(
            access_token=access_token, client_secret=CONFIG['client_secret'])
        session['access_token'] = access_token
    except Exception as e:
        print(e)
    # return "<a href='/get-user-likes'>Get photos liked by user</a>"
    return redirect('/get-user-likes')


@app.route('/get-user-likes')
def get_user_likes():
    access_token = session['access_token']

    if not access_token:
        return render_template('error.html', error="Missing Access Token")

    api = client.InstagramAPI(
        access_token=access_token, client_secret=CONFIG['client_secret'])
    recent_media, next_ = api.user_liked_media()

    photos = []
    for media in recent_media:
        photos.append(media.images['standard_resolution'].url)

    tags = get_common_tags(photos)
    rec = get_etsy_products(tags)
    r = get_all_images(rec)

    return render_template('product-suggest.html', recs=r)


@app.errorhandler(404)
def error(error):
    return render_template('error.html', error=error), 404
