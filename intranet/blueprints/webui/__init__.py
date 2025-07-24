from flask import Blueprint

from .views import index, hour

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/hour/<hour>", view_func=hour, endpoint="hourview")

def init_app(app):
    app.register_blueprint(bp)
