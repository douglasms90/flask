from flask import render_template, request
from datetime import date, timedelta
import flask_excel as excel

from app import app
from app.models.tables import databaseConnection


@app.route("/support", methods = ["GET", "POST"])
def support():
  connect = databaseConnection("dbname='' user='' host='' password=''")
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
