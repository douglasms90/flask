from flask import render_template, redirect, url_for
from intranet.models import MessageForm

def index():
    booked_hours = ["11:00", "12:00"]  # exemplo vindo do servidor
    return render_template('index.html', booked_hours=booked_hours, date=[8, 9, 10, 11, 12])

def hour():
    form = MessageForm()
    if form.validate_on_submit():
        return render_template("hour.html")
    return render_template('hour.html')
