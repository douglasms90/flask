from flask import render_template, redirect, url_for
from datetime import datetime
from intranet.ext.database import db, dbc
from intranet.ext.webscraping import bs
from intranet.models import Act, Vln, MessageForm
from decouple import config


def index():
    form = MessageForm()
    if form.validate_on_submit():
        split = form.msg.data.split()
        db.session.add(
            Act(
                dt=datetime.now(),
                req=form.msg.data,
                sn=split[-3],
                vln=Vln.query.filter_by(olt=split[1], tfc=split[4]).first().vln,
                ctr=split[-2],
                cto=split[-1],
            )
        )
        db.session.commit()
        return redirect(url_for("webui.index"))
    return render_template("index.html", form=form, historic=Act.query.filter(Act.dt.startswith(datetime.now().date())).all(),
        tittl = ['Id','Data e Hora','Requisição','Commando','SN','Vlan','Contrato','CTO'])

def na():
    conn = dbc(config("host"))
    return render_template("table.html", rows = conn.consult(config("naquery")), titl = ['ID', 'NOME', 'CIDADE', 'BAIRRO', 'DESCRIÇÃO'])

def re():
    conn = dbc(config("host"))
    return render_template("table.html", rows = conn.consult(config("requery")), titl = ['ID', 'NOME', 'CIDADE', 'BAIRRO', 'DESCRIÇÃO'])
