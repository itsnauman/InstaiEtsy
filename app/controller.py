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

def update_user_tags_and_recs(tag_list):
	for tag in tag_list:
		user_tags[tag] = 0

def update_rankings(user_tags, tag_list):
	for key, val in user_tags:
		for list_tag in tag_list:
			if key==list_tag:
				++user_recs[key]

# def get_etsy_results_ml(user_tags, tag_list):
# 	"""
#     Returns a list of Etsy product listings based on image recognition results.
#     """
# 	#sorted by values (rank)
# 	sorted_user_tags = sorted(user_tags.items(), key=operator.itemgetter(1))

# 	for key, val in user_tags:
# 		for list_tag in tag_list:
# 			if (key==list_tag) &&:

#     	#do something with Etsy API

def get_etsy_products(tag_list):
    """
    Returns a list of all the matching items currenly on sale at Etsy
    """
    payload = {'api_key': ETSY_API_KEY, 'keywords': tag_list}
    res = requests.get('https://openapi.etsy.com/v2/listings/active', params=payload)
    return res.text

@app.route('/')
def index():
    print get_etsy_products()
    return "Hello World"
