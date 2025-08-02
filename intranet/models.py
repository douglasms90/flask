from intranet.ext.database import db

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    msg = StringField('formatted_hour', validators=[DataRequired()])
    submit = SubmitField('Send')

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nm = db.Column(db.String(100), nullable=False)
    dt = db.Column(db.DateTime, nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.Numeric())
    description = db.Column(db.Text)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
