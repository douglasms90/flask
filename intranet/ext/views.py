from flask import render_template, request
from datetime import date, timedelta
import flask_excel as excel

from intranet.ext import database


def init_app(app):
  @app.route("/home")
  @app.route("/")
  def home():
    return render_template("home.html", home = "CONTEÚDO HOME")

  '''@app.route("/login", methods = ["GET", "POST"])
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
    return redirect(url_for("home.html"))'''


  # BACKOFFICE

  @app.route("/backoffice", methods = ["GET"])
  def backoffice():
    connect = database()
    database = connect.consult("""SELECT os.codos, df.descricao_defeito, tp.descricao, os.data_fechamento, cl.nome_razaosocial, os.operador_fech_tecnico, os.servico_prestado
      FROM mk_os os
      FULL OUTER JOIN mk_os_tipo tp ON os.tipo_os = tp.codostipo
      JOIN mk_pessoas cl ON os.cliente = cl.codpessoa
      JOIN mk_os_defeitos df ON os.defeito_associado = df.coddefeito
      WHERE  tipo_os in ('4','15','18') AND data_fechamento = CURRENT_DATE AND servico_prestado LIKE '%ug%' ORDER BY os.data_fechamento desc""")
    connect.close()
    return render_template("backoffice.html", rows = database)


  # SUPPORT

  @app.route("/support", methods = ["GET", "POST"])
  def support():
    connect = database()
    database = connect.consult("""SELECT os.codos, df.descricao_defeito, tp.descricao, os.data_abertura, cl.nome_razaosocial, cd.cidade, ba.bairro
      FROM mk_os os
      FULL OUTER JOIN mk_os_tipo tp ON os.tipo_os = tp.codostipo
      JOIN mk_pessoas cl ON os.cliente = cl.codpessoa
      JOIN mk_os_defeitos df ON os.defeito_associado = df.coddefeito
      JOIN mk_cidades cd ON os.cd_cidade = cd.codcidade
      JOIN mk_bairros ba ON os.cd_bairro = ba.codbairro
      WHERE status='1' AND tipo_os in ('4','15','18') AND fechamento_tecnico='N' ORDER BY cd.cidade asc""")
    connect.close()

    tomorrow = date.today() + timedelta(days=1)

    if request.method == "POST":
      return excel.make_response_from_array(database, "xlsx", file_name = tomorrow.strftime('%d.%m.%Y'))
    return render_template("support.html", rows = database)
