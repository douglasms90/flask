from flask import Blueprint

from .views import index, booking

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/booking/<booking_id>", view_func=booking, endpoint="bookingview")

def init_app(app):
    app.register_blueprint(bp)
