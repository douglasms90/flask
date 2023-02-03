from flask import abort, render_template

from intranet.ext.database import dbc
from dotenv import load_dotenv
from os import getenv


load_dotenv()
host = getenv('host')
osquery = getenv('osquery')
requery = getenv('requery')

def index():
    return render_template("index.html")

def na():
    conn = dbc(host)
    return render_template("os.html", rows = conn.consult(osquery))

def re():
    conn = dbc(host)
    return render_template("os.html", rows = conn.consult(requery))
