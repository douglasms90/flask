from intranet.ext.database import db

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    msg = StringField('formatted_hour', validators=[DataRequired()])
    submit = SubmitField('Send')
