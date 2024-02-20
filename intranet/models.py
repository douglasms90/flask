from intranet.ext.database import db

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    msg = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

class Atv(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tp = db.Column(db.String(20))
    nm = db.Column(db.String(10))
    pm = db.Column(db.Float(10))
    qt = db.Column(db.Float(10))
    rc = db.Column(db.String(10))
    pa = db.Column(db.Float(10))
