from . import app, clarifai_api, ETSY_API_KEY
from flask import render_template, request, session
from instagram.client import InstagramAPI
import requests
from instagram import client

user_tags = {}

CONFIG = {
    'client_id': '5d99f0fac1084de5a71f889452248123',
    'client_secret': 'aba8aa200eaf417ca9ef54a9b83eddfd',
    'redirect_uri': 'https://172e3628.ngrok.com/insta-auth'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)

def get_user_instagram_likes(user_id, count=10, max_id="max_id"):
	"""
    Returns a list of all the recently liked media by the Instagram user.
    """
	recent_likes, next_ = insta_api.user_recent_media(user_id, count, max_id)
	liked_media = []
	for like in recent_likes:
	   liked_media.append('<img src="%s"/>' % media.images['thumbnail'].url)
	
    return liked_media

def get_tags_for_photo(photo_url):
    """
    Returns a list of all the tags for a photo using clarifai's
    image recognition.
    """
    result = clarifai_api.tag_image_urls(photo_url)
    tag_list = result['results'][0]['result']['tag']['classes']
    return tag_list

def update_user_tags(tag_list):
	for tag in tag_list:
		user_tags[tag] = 0

def update_user_rankings_ML(user_tags, tag_list):
	for key, val in user_tags:
		for list_tag in tag_list:
			if key==list_tag:
				++user_recs[key]

def keywordAlgo(liked_media):
    rough = []
    master = {}
    master[rough[0]] = 0
    for i in range(0,4):
        range.append(tag5(get_tags_for_photo(liked_media[i])))

    for element in rough:
        if not element in master:
            master[element] = 1
        else:
            master[element] += 1

    return (master)

def tag5(long):
    short = [long[i] for i in (0,1,2,3,4)]
    return short

def get_etsy_products():
    """
    Returns a list of all the matching items currently on sale at Etsy
    """
    payload = {'api_key': ETSY_API_KEY, 'keywords': 'cats'}
    res = requests.get('https://openapi.etsy.com/v2/listings/active', params=payload)
    return res.text

@app.route('/')
def index():
<<<<<<< HEAD
    print(keywordAlgo())
    return "Hello World"
=======
    try:
        url = unauthenticated_api.get_authorize_url(scope=["likes","comments"])
        return '<a href="%s">Connect with Instagram</a>' % url
    except Exception as e:
        print(e)

@app.route('/insta-auth')
def on_callback():
    code = request.args.get("code")
    if not code:
        return 'Missing code'
    try:
        access_token, user_info = unauthenticated_api.exchange_code_for_access_token(code)
        if not access_token:
            return 'Could not get access token'
        api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
        session['access_token'] = access_token
    except Exception as e:
        print(e)
    return "<a href='/get-user-likes'>Get photos liked by user</a>"

@app.route('/get-user-likes')
def user_likes():
    access_token = session['access_token']
    if not access_token:
        return 'Missing Access Token'
    api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
    recent_media, next_ = api.user_liked_media()
    photos = []
    for media in recent_media:
        photos.append('<img src="%s"/>' % media.images['thumbnail'].url)

    print photos
    return "hello world"
>>>>>>> origin
