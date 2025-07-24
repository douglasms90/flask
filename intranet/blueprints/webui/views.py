from flask import render_template


def index():
    booked_hours = ["11:00", "12:00", "13:00"]  # exemplo vindo do servidor
    return render_template('index.html', booked_hours=booked_hours)

def hour(hour):
    return render_template('hour.html', formatted_hour=hour)
