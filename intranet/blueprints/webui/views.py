from flask import render_template, redirect, url_for
from intranet.models import MessageForm


def index():
    form = MessageForm()
    if form.validate_on_submit():
        return render_template("table.html", form=form)
    return render_template("index.html", form=form)
