from flask import render_template, request
from datetime import date, timedelta
import flask_excel as excel


def init_app(app, db):
  @app.route("/")
  def home():
    return render_template("home.html", home = "CONTEÚDO HOME")

  # BACKOFFICE

  @app.route("/backoffice", methods = ["GET"])
  def backoffice():
    consult = ("""SELECT os.codos, df.descricao_defeito, tp.descricao, os.data_fechamento, cl.nome_razaosocial, os.operador_fech_tecnico, os.servico_prestado
      FROM mk_os os
      FULL OUTER JOIN mk_os_tipo tp ON os.tipo_os = tp.codostipo
      JOIN mk_pessoas cl ON os.cliente = cl.codpessoa
      JOIN mk_os_defeitos df ON os.defeito_associado = df.coddefeito
      WHERE  tipo_os in ('4','15','18') AND data_fechamento = CURRENT_DATE AND servico_prestado LIKE '%ug%' ORDER BY os.data_fechamento desc""")
    return render_template("backoffice.html", rows = db)

  # SUPPORT

  @app.route("/support", methods = ["GET", "POST"])
  def support():
    tomorrow = date.today() + timedelta(days=1)
    if request.method == "POST":
      return excel.make_response_from_array(db, "xlsx", file_name = tomorrow.strftime('%d.%m.%Y'))
    return render_template("support.html", rows = db)