from flask import render_template, redirect, url_for
from intranet.models import MessageForm

def index():
    form = MessageForm()
    booked_hours = ["12:00", "13:00"]  # exemplo vindo do servidor
    if form.validate_on_submit():
        return render_template("index.html", form=form)
    return render_template('index.html', booked_hours=booked_hours)
