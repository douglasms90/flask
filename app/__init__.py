from flask import Flask


app = Flask(__name__)


from app.models import tables, forms
from app.controllers import default, suporte
