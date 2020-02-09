from app import app
from flask import render_template


@app.route("/home")
@app.route("/")
def home():
  return render_template("home.html", home = 'CONTEÚDO HOME')