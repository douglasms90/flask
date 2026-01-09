from flask import abort, render_template
from intranet.models import Booking
from collections import defaultdict

def index():
    bookings = Booking.query.order_by(Booking.dt).all()
    grouped_bookings = defaultdict(list)
    for booking in bookings:
        day = booking.dt.date()  # extrai apenas a data
        grouped_bookings[day].append(booking)
    print(grouped_bookings)
    return render_template("index.html", grouped_bookings=grouped_bookings)

def booking(booking_id):
    booking = Booking.query.filter_by(id=booking_id).first() or abort(404, "horário nao encontrado")
    return render_template("booking.html", booking=booking)


