from flask import abort, render_template

from intranet.ext.database import dbConn
from intranet.ext.forms import commForms


def index():
  form = commForms()
  conn = dbConn()
  if form.comm.data == 'os':
    rows = conn.consult("""""")
    title = ('ID', 'DEFEITO', 'TIPO', 'GERADA', 'CLIENTE', 'CIDADE', 'BAIRRO') 
    return render_template("index.html", form=form, rows = rows, ts = title)
  if form.comm.data == 're':
    rows = conn.consult("""""")
    title = ('ID', 'DEFEITO', 'DESCRIÇÃO', 'FECHAMENTO', 'CLIENTE', 'OPERADOR', 'DESCRIÇÃO')
    return render_template("index.html", form=form, rows = rows, ts = title)
  return render_template("index.html", form=form)
