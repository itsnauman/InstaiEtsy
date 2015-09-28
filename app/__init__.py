from flask import Flask
from clarifai.client import ClarifaiApi
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

CONFIG = {
    'client_id': app.config['INSTA_CLIENT_ID'],
    'client_secret': app.config['INSTA_CLIENT_SECRET'],
    'redirect_uri': app.config['INSTA_REDIRECT_URI']
}

ETSY_API_KEY = app.config['ETSY_API']

clarifai_api = ClarifaiApi(app_id=app.config['CLARIFAI_API'], app_secret=app.config['CLARIFAI_SECRET'])

from . import controller
