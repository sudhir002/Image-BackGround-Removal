__author__ = 'Sudhir'
__date__ = "Aug 3 - 2021"

'''
Purpose : define the application and uses.
'''

from flask import Flask
from flask_cors import CORS


application = Flask(__name__, static_url_path='/static', static_folder="database/")
application.config['SECRET_KEY'] = 'hardsecretkey'
CORS(application)

# prevent cached responses
if application.config["DEBUG"]:
    @application.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response