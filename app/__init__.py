from flask import Flask
from clarifai.client import ClarifaiApi
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.secret_key = 'very_secret_key'
# Instagram API Details
access_token = "5d99f0fac1084de5a71f889452248123"
client_secret = "aba8aa200eaf417ca9ef54a9b83eddfd"

ETSY_API_KEY = "g3kguayhagkdmstc7f6hnaa2"

clarifai_api = ClarifaiApi(app_id="EnSVY5w5DxxvH2Fq-XrkHbdtge5favWmTNybItti", app_secret="TFlBASaMNs8S4VzRsxXQUQeMPoW46T9KbGXkzD3V")

from . import controller
