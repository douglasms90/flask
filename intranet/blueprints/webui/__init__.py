from flask import Blueprint

from .views import index, na, re

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/na", view_func=na)
bp.add_url_rule("/re", view_func=re)

def init_app(app):
  app.register_blueprint(bp)