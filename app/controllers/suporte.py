from flask import render_template, request, redirect, url_for
from app import app
from datetime import date, timedelta
from os import makedirs, path
import webbrowser

from app.models.tables import databaseConnection
from app.models.forms import dumpData
from app.models.worksheet import createWorksheet


@app.route("/suporte", methods = ["GET", "POST"])
def suporte():
  data = date.today() + timedelta(days=1)

  dt_month = data.strftime('%m.%Y')
  dt_file = data.strftime('%d.%m.%Y')
  tomorrow = data.strftime('%d/%m/%Y')
  
  connect = databaseConnection("dbname='mkData3.0' user='cliente_r' host='177.184.72.6' password='Cl13nt_R'")
  data = dumpData()
  database = connect.Consult("""SELECT os.codos, cl.cd_empresa, tp.descricao, os.data_abertura, cl.nome_razaosocial, cd.cidade, ba.bairro, lo.logradouro, df.descricao_defeito
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
    path_xlsx = '/home/douglas/Python/newproject/app/static/suporte/model.xlsx'
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

"""
SELECT os.codos, df.descricao_defeito, at.dt_abertura, os.data_abertura,cd.cidade, ba.bairro, lo.logradouro, cl.nome_razaosocial, os.defeito_reclamado
FROM mk_os os
JOIN mk_os_defeitos df ON os.defeito_associado = df.coddefeito
FULL OUTER JOIN mk_atendimento at ON os.protocolo_os = at.protocolo
JOIN mk_cidades cd ON os.cd_cidade = cd.codcidade
JOIN mk_bairros ba ON os.cd_bairro = ba.codbairro
JOIN mk_logradouros lo ON os.cd_logradouro = lo.codlogradouro
JOIN mk_pessoas cl ON os.cliente = cl.codpessoa
WHERE status='1' AND tipo_os in ('4','15') ORDER BY os.codos asc
"""