from intranet.ext.database import db

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    msg = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

class Act(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dt = db.Column(db.DateTime(20))
    req = db.Column(db.String(200))
    sn = db.Column(db.String(20))
    vln = db.Column(db.Numeric(5))
    ctr = db.Column(db.Numeric(10))
    cto = db.Column(db.String(5))

class Vln(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    olt = db.Column(db.String(20))
    tfc = db.Column(db.String(10))
    vln = db.Column(db.Numeric(5))
