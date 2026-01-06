from flask import abort, render_template
from intranet.models import Booking


def index():
    bookings = Booking.query.all()
    return render_template("index.html", bookings=bookings)

def booking(booking_id):
    booking = Booking.query.filter_by(id=booking_id).first() or abort(404, "horário nao encontrado")
    return render_template("booking.html", booking=booking)
