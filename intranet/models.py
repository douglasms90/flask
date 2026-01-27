from intranet.ext.database import db

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    msg = StringField('formatted_hour', validators=[DataRequired()])
    submit = SubmitField('Send')

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dt = db.Column(db.DateTime, nullable=False)
    nm = db.Column(db.String(100), nullable=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))

class Assets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cl = db.Column(db.String(20))
    nm = db.Column(db.String(20))
    pr = db.Column(db.Float)
    pm = db.Column(db.Float)
    qt = db.Column(db.Float)
    dv = db.Column(db.Float)
    pl = db.Column(db.Float)
    vp = db.Column(db.Float)
