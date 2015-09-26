from . import app, clarifai_api, ETSY_API_KEY
from flask import render_template
import requests
from pprint import pprint

from instagram.client import InstagramAPI

access_token = "e028ff7d074940f087f6248c9df7b3a9"
client_secret = "c8450b5e4dc54ef4afe2b0040a1ee546"
insta = InstagramAPI(access_token=e028ff7d074940f087f6248c9df7b3a9, client_secret=c8450b5e4dc54ef4afe2b0040a1ee546)

def get_user_insta_liked_media(userID="user_id"):
	"""
    Returns a list of all the tags for a photo using clarifai's
    image recognition.
    """
	recent_likes, next_ = api.user_recent_media(user_id, count, max_id)
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

def get_etsy_products():
    payload = {'api_key': ETSY_API_KEY}
    res = requests.get('')

@app.route('/')
def index():
    return "Hello World"
