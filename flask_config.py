from flask import Flask
from flask_cors import CORS


application = Flask(__name__, static_url_path='/static', static_folder="database/")
application.config['SECRET_KEY'] = 'hardsecretkey'
CORS(application)
