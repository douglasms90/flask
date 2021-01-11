from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.tables import User
from app.models.forms import LoginForm


@lm.user_loader
def load_user(id):
  return User.query.filter_by(id = id).first()

@app.route("/home")
@app.route("/")
def home():
  return render_template("home.html", home = "CONTEÚDO HOME")

@app.route("/login", methods = ["GET", "POST"])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username = form.username.data).first()
    if user and user.password == form.password.data:
      login_user(user)
      flash("Logado")
      return redirect(url_for("home"))
    else:
      flash("Inválido")
  return render_template("login.html", form = form)
 
@app.route("/logout")
def logout():
  logout_user()
  flash("Logged out.")
  return redirect(url_for("home.html"))
