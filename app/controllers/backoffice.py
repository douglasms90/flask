from flask import render_template

from app import app
from app.models.tables import databaseConnection


@app.route("/backoffice", methods = ["GET", "POST"])
def backoffice():
  connect = databaseConnection("dbname='mkData3.0' user='cliente_r' host='177.184.72.6' password='Cl13nt_R'")
  database = connect.consult("""SELECT os.codos, os.data_abertura, cl.nome_razaosocial, cd.cidade, ba.bairro, lo.logradouro, os.num_endereco, os.operador
		FROM mk_os os
		JOIN mk_pessoas cl ON os.cliente = cl.codpessoa
		JOIN mk_cidades cd ON os.cd_cidade = cd.codcidade
		JOIN mk_bairros ba ON os.cd_bairro = ba.codbairro
		JOIN mk_logradouros lo ON os.cd_logradouro = lo.codlogradouro
		WHERE status='1' AND tipo_os in ('7','8','9','10') AND fechamento_tecnico='N' ORDER BY cd.cidade asc""")

  def dumpData(database):
    obj_list = list()
    count = 0
    for data in database:
      ob = dict()
      count += 1
      ob["column1"] = count # Quantos
      ob["column2"] = data[0] # Id
      if data[1]:
        ob["column3"] = data[1].strftime("%d/%m/%Y") # Gerada
      else:
        ob["column3"] = "X"
      ob["column4"] = data[2] # Cliente
      ob["column5"] = data[3] # Cidade
      ob["column6"] = data[4].title() # Bairro
      ob["column7"] = data[5].title() # Logradouro
      ob["column8"] = data[6] # Número
      ob["column9"] = data[7].title() # Operador
      obj_list.append(ob)
    return obj_list

  obj_list = dumpData(database)
  return render_template("backoffice.html", rows = obj_list)
