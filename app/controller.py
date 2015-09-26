from . import app, clarifai_api
from flask import render_template
from pprint import pprint

def get_tags_for_photo(photo_url):
    """
    Returns a list of all the tags for a photo using clarifai's
    image recognition.
    """
    result = clarifai_api.tag_image_urls(photo_url)
    tag_list = result['results'][0]['result']['tag']['classes']
    return tag_list

@app.route('/')
def index():
    return "Hello World"
