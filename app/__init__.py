from flask import Flask
from clarifai.client import ClarifaiApi
from instagram.client import InstagramAPI

app = Flask(__name__)

access_token = "e028ff7d074940f087f6248c9df7b3a9"
client_secret = "c8450b5e4dc54ef4afe2b0040a1ee546"
ETSY_API_KEY = "g3kguayhagkdmstc7f6hnaa2"

clarifai_api = ClarifaiApi(app_id="EnSVY5w5DxxvH2Fq-XrkHbdtge5favWmTNybItti", app_secret="TFlBASaMNs8S4VzRsxXQUQeMPoW46T9KbGXkzD3V")
insta_api = InstagramAPI(access_token=access_token, client_secret=client_secret)

from . import controller
