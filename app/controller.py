from . import app, clarifai_api, ETSY_API_KEY
from flask import render_template
import requests
from pprint import pprint
from instagram.client import InstagramAPI

user_tags = {}

access_token = "e028ff7d074940f087f6248c9df7b3a9"
client_secret = "c8450b5e4dc54ef4afe2b0040a1ee546"
insta_api = InstagramAPI(access_token=e028ff7d074940f087f6248c9df7b3a9, client_secret=c8450b5e4dc54ef4afe2b0040a1ee546)

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

<<<<<<< HEAD
def get_etsy_results_simple(tag_list):
	"""
    Returns a list of Etsy product listings based on image recognition results.
    """
    for tag in tag_list:
    	#do something with Etsy API

def update_user_tags_and_recs(tag_list):
	for tag in tag_list:
		user_tags[tag] = 0

def update_rankings(user_tags, tag_list):
	for key, val in user_tags:
		for list_tag in tag_list:
			if key==list_tag:
				++user_recs[key]

def get_etsy_results_ml(user_tags, tag_list):
	"""
    Returns a list of Etsy product listings based on image recognition results.
    """

    """
    values = list(d.values())
	max_rank = max(values)
	max_rank_index = values.index(max_value)
	"""
	#sorted by values (rank)
	sorted_user_tags = sorted(user_tags.items(), key=operator.itemgetter(1))

	for key, val in user_tags:
		for list_tag in tag_list:
			if (key==list_tag) &&:

    	#do something with Etsy API

=======
def get_etsy_products():
    payload = {'api_key': ETSY_API_KEY}
    res = requests.get('')
>>>>>>> 1fabec0d75ac7c0297233d9d0950713fdfe2288a

@app.route('/')
def index():
    return "Hello World"
