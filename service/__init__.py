from flask import Flask, Blueprint
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, origins='*')
app.config['CORS_HEADERS'] = 'Content-Type'

app.app_context().push()

from service import routes