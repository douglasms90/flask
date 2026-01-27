from flask import Blueprint

from .views import index, booking, assets

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/booking/<booking_id>", view_func=booking, endpoint="bookingview")
bp.add_url_rule("/assets", view_func=assets)

def init_app(app):
    app.register_blueprint(bp)
