from . import app, clarifai_api, ETSY_API_KEY, insta_api
from flask import render_template
import requests
from pprint import pprint

user_tags = {}

def get_user_insta_liked_media(USERID="user_id", COUNT=10, MAX_ID="max_id"):
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
    print(keywordAlgo())
    return "Hello World"
