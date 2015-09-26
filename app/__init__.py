from flask import Flask
from clarifai.client import ClarifaiApi

app = Flask(__name__)
clarifai_api = ClarifaiApi(app_id="EnSVY5w5DxxvH2Fq-XrkHbdtge5favWmTNybItti", app_secret="TFlBASaMNs8S4VzRsxXQUQeMPoW46T9KbGXkzD3V")
from . import controller
