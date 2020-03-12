# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, abort, redirect, jsonify, g, url_for
import datetime, time
from os_script import findos
from os_script import teste
from prod import main, checkAgain
from alerta import inicio
from travapon import selectUsers
from router import getUser
from contrato import getContrato, checkConection
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.secret_key = os.urandom(24)


# @app.route('/padmin')
# def padmin():
#   return render_template('CP.padmin.html')

@app.route('/')
def index():
 if g.user:
  return render_template('index.html')
 return redirect(url_for('login'))

@app.route('/new')
def new():
  return render_template('new.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
     session.pop('user', None)
     username = request.form['username']
     password = request.form['password']
     users = selectUsers(username,password)   
     if users:
      session['user'] = request.form['username']
      return redirect(url_for('index'))

    return render_template('login.html')

##################
@app.route('/map')
def map():
  if g.user:
   return render_template('map.html')
  return redirect(url_for('index'))

@app.route('/blank')
def blank():
  if g.user:
   return render_template('blank.html')
  return redirect(url_for('index')) 

@app.route('/ajaxConexao',methods=['POST'])
def ajaxConexao():
  if g.user:
    if request.method == 'POST':
      con = request.form['contrato']
      statusconexao = checkConection(con)
      return jsonify(status=statusconexao)
  return redirect(url_for('index'))   

@app.route('/ajaxPage',methods=['POST'])
def ajaxPage():
  if g.user: 
   if request.method == 'POST':
    con = request.form['contratotxt']
    contrato = getContrato(con)
    contratoUser = checkConection(contrato[0][6])    
    return jsonify(dados=contrato,conexao=contratoUser)
  return redirect(url_for('index')) 
################


@app.route('/test')
def test():
  return render_template('test.html')

@app.route('/alerta')
def alerta():
  if g.user:
   row = inicio()
   return render_template('alerta.html',data=row)
  return redirect(url_for('login'))
  
@app.route('/ppdetalhes')
def ppdetalhes():
 if g.user:
  return render_template('ppdetalhes.html')
 return redirect(url_for('login'))

colPP = [
  {
    "field": "NOME", # which is the field's name of data key 
    "title": "NOME", # display as the table header's name
    "sortable": True,
  },
  {
    "field": "BAIRRO",
    "title": "BAIRRO",
    "sortable": True,
  },
  {
    "field": "STATUS",
    "title": "STATUS",
    "sortable": True,
  }
]

@app.route('/equipments')
def equipments():
 if g.user:
  return render_template('equipments.html',data='teste',columns=colPP,title='Equipamentos')
 return redirect(url_for('login'))

##############################################
@app.route('/ajaxUser',methods=['POST'])
def ajaxUser():
 if request.method == 'POST':
  var = 'secondajax'
  return jsonify(resultado=var)   

@app.route('/ajaxPP',methods=['POST'])
def ajaxPP():
  if g.user: 
   if request.method == 'POST':
    us = request.form['search-input']
    user = getUser(us)
    return jsonify(result=user)
  return redirect(url_for('index'))  
#################################################

@app.route('/network',methods=['POST','GET'])
def network():
 if g.user:
  if request.method == 'POST':
   return render_template('network.html')
  else:
   return render_template('network.html')
 return redirect(url_for('login'))

col = [
  {
    "field": "HORARIO", # which is the field's name of data key 
    "title": "HORARIO", # display as the table header's name
    "sortable": True,
  },
  {
    "field": "BAIRRO",
    "title": "BAIRRO",
    "sortable": True,
  },
  {
    "field": "RUA",
    "title": "RUA",
    "sortable": True,
  },
  {
    "field": "NUMERO",
    "title": "NUMERO",
    "sortable": True,
  },
  {
    "field": "USERNAME",
    "title": "USERNAME",
    "sortable": True,
  },
  {
    "field": "CONTRATO",
    "title": "CONTRATO",
    "sortable": True,
  }
]

@app.route('/pacpon', methods=['POST','GET'])
def pacpon(): 
 if g.user:
   rows = main()
   return render_template("pacpon.html", data=rows, columns=col, title='PAC PONs')
 return redirect(url_for('login'))

@app.route('/listaos')
def listaos():
 if g.user:   
  return render_template('listaos.html')
 return redirect(url_for('login'))

#@app.route('/listaos')
#def listaos():
#return render_template('listaos.html')

columns = [
  {
    "field": "ID", # which is the field's name of data key 
    "title": "ID", # display as the table header's name
    "sortable": True,
  },
  {
    "field": "DEFEITO",
    "title": "DEFEITO",
    "sortable": True,
  },
  {
    "field": "CLIENTE",
    "title": "CLIENTE",
    "sortable": True,
  },
  {
    "field": "CIDADE",
    "title": "CIDADE",
    "sortable": True,
  },
  {
    "field": "BAIRRO",
    "title": "BAIRRO",
    "sortable": True,
  },
  {
    "field": "RUA",
    "title": "RUA",
    "sortable": True,
  },
  {
    "field": "NUMERO",
    "title": "NUMERO",
    "sortable": True,
  },
  {
    "field": "CONTRATO",
    "title": "CONTRATO",
    "sortable": True,
  },
  {
    "field": "USERNAME",
    "title": "USERNAME",
    "sortable": True,
  },
  {
    "field": "PROBLEMA",
    "title": "PROBLEMA",
    "sortable": True,
  }
]

#jdata=json.dumps(data)

@app.route('/os', methods=['POST','GET'])
def table():
  if g.user:
   dataabertura = datetime.date.today()
   if request.method == 'POST':
    dataabertura = request.form['dataabertura']
    rows = findos(dataabertura)	
    return render_template("table.html", data=rows, columns=columns, title='Ordens de Serviços')
   else:
    dataabertura = datetime.date.today() 
    rows = findos(dataabertura)	
    return render_template("table.html", data=rows, columns=columns, title='Ordens de Serviços')
  return redirect(url_for('login'))

@app.before_request
def before_request():
    g.user = None
    app.permanent_session_lifetime = datetime.timedelta(minutes=10000)
    if 'user' in session:
        g.user = session['user']

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
