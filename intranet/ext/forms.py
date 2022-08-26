from flask_wtf import FlaskForm
from wtforms import StringField


class commForms(FlaskForm):
  comm = StringField("comm")