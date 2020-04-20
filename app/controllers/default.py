from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user
from os import makedirs, path
from datetime import date, timedelta
from app import app, db, lm
import webbrowser


from app.models.tables import User, databaseConnection
from app.models.worksheet import createWorksheet
from app.models.forms import LoginForm, dumpData


@lm.user_loader
def load_user(id):
  return User.query.filter_by(id = id).first()

# HOME
@app.route("/home")
@app.route("/")
def home():
  return render_template("home.html", home = 'CONTEÚDO HOME')

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
 
# LOGOUT
@app.route("/logout")
def logout():
  logout_user()
  flash("Logged out.")
  return redirect(url_for("home.html"))

# SUPORTE
@app.route("/suporte", methods = ["GET", "POST"])
def suporte():
  data = date.today() + timedelta(days=1)

  dt_month = data.strftime('%m.%Y')
  dt_file = data.strftime('%d.%m.%Y')
  tomorrow = data.strftime('%d/%m/%Y')
  
  connect = databaseConnection("dbname='mkData3.0' user='cliente_r' host='177.184.72.6' password='Cl13nt_R'")
  data = dumpData()
  database = connect.Consult("""SELECT os.codos, df.descricao_defeito, tp.descricao, os.data_abertura, cl.nome_razaosocial, cd.cidade, ba.bairro, lo.logradouro
    FROM mk_os os
    FULL OUTER JOIN mk_os_tipo tp ON os.tipo_os = tp.codostipo
    JOIN mk_pessoas cl ON os.cliente = cl.codpessoa
    JOIN mk_os_defeitos df ON os.defeito_associado = df.coddefeito
    JOIN mk_cidades cd ON os.cd_cidade = cd.codcidade
    JOIN mk_bairros ba ON os.cd_bairro = ba.codbairro
    JOIN mk_logradouros lo ON os.cd_logradouro = lo.codlogradouro
    WHERE status='1' AND tipo_os in ('4','15') ORDER BY cd.cidade asc""")
  obj_list = data.dumpData(database, tomorrow)
  if request.method == "POST":
    path_xlsx = '/home/douglas/Python/intranet/app/static/suporte/model.xlsx'
    path_folder = f'/home/douglas/Documentos/worksheet/{dt_month}'
    path_file = f'{path_folder}/{dt_file}.xlsx'
    if path.isdir(path_folder):
      pass
    else:
      makedirs(path_folder)
    create = createWorksheet(path_xlsx)
    create.add_into_sheet(obj_list)
    create.save(path_file)
    connect.close()
    webbrowser.open(path.abspath(path_file))
  return render_template("suporte.html", rows = obj_list)