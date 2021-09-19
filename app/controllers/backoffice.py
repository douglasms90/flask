from flask import render_template
from datetime import date, timedelta
import flask_excel as excel

from app import app
from app.models.tables import databaseConnection


@app.route("/backoffice", methods = ["GET", "POST"])
def backoffice():
  connect = databaseConnection("dbname='mkData3.0' user='cliente_r' host='177.184.72.6' password='Cl13nt_R'")
  database = connect.consult("""SELECT os.codos, df.descricao_defeito, tp.descricao, os.data_abertura, cl.nome_razaosocial, cd.cidade, ba.bairro, lo.logradouro, os.num_endereco, os.operador
    FROM mk_os os
    FULL OUTER JOIN mk_os_tipo tp ON os.tipo_os = tp.codostipo
    JOIN mk_pessoas cl ON os.cliente = cl.codpessoa
    JOIN mk_os_defeitos df ON os.defeito_associado = df.coddefeito
    JOIN mk_cidades cd ON os.cd_cidade = cd.codcidade
    JOIN mk_bairros ba ON os.cd_bairro = ba.codbairro
    JOIN mk_logradouros lo ON os.cd_logradouro = lo.codlogradouro
    WHERE status='1' AND tipo_os in ('4','15','18') AND fechamento_tecnico='N' ORDER BY cd.cidade asc""")
  connect.close()
  return render_template("backoffice.html", rows = database)
