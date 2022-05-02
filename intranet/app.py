from flask import Flask
import flask_excel as excel

from intranet.ext import config
from intranet.ext import appearance
from intranet.ext import database
from intranet.ext import views

app = Flask(__name__)

config.init_app(app)
appearance.init_app(app)
database.init_app(app)
views.init_app(app)
