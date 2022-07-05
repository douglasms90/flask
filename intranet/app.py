from flask import Flask
from intranet.ext import config


def create_app():
  app = Flask(__name__)
  config.init_app(app)
  config.load_extensions(app)
  return app