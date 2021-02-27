from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
import flask_excel as excel

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

lm = LoginManager()

lm.init_app(app)

from app.models import tables, forms, worksheets
from app.controllers import default, suporte, backoffice
