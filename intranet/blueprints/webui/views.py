from flask import abort, render_template, request
from datetime import date, timedelta
import flask_excel as excel

from intranet.ext.database import dbConn


def index():
  return render_template("index.html")

def na():
  conn = dbConn()
  dbOsNaDumps = conn.consult("""SELECT os.codos, df.descricao_defeito, tp.descricao, os.data_abertura, cl.nome_razaosocial, cd.cidade, ba.bairro
    FROM mk_os os
    FULL OUTER JOIN mk_os_tipo tp ON os.tipo_os = tp.codostipo
    JOIN mk_pessoas cl ON os.cliente = cl.codpessoa
    JOIN mk_os_defeitos df ON os.defeito_associado = df.coddefeito
    JOIN mk_cidades cd ON os.cd_cidade = cd.codcidade
    JOIN mk_bairros ba ON os.cd_bairro = ba.codbairro
    WHERE status='1' AND tipo_os in ('4','15','18') AND fechamento_tecnico='N' ORDER BY cd.cidade asc""") or abort(404, "Não tem os")
  conn.close()
  if request.method == "POST":
    tomorrow = date.today() + timedelta(days=1)
    return excel.make_response_from_array(dbOsNaDumps, "xlsx", file_name = tomorrow.strftime('%d.%m.%Y'))
  return render_template("osNa.html", rows = dbOsNaDumps)   

def re():
  conn = dbConn()
  dbOsFiDumps = conn.consult("""SELECT os.codos, df.descricao_defeito, tp.descricao, os.data_fechamento, cl.nome_razaosocial, os.operador_fech_tecnico, os.servico_prestado
    FROM mk_os os
    FULL OUTER JOIN mk_os_tipo tp ON os.tipo_os = tp.codostipo
    JOIN mk_pessoas cl ON os.cliente = cl.codpessoa
    JOIN mk_os_defeitos df ON os.defeito_associado = df.coddefeito
    WHERE  tipo_os in ('4','15','18') AND data_fechamento = CURRENT_DATE AND servico_prestado LIKE '%ugl%' ORDER BY os.data_fechamento desc""") or abort(404, "Não tem o.s para reagendar com o nome: Douglas")
  conn.close()
  return render_template("osFi.html", rows = dbOsFiDumps)