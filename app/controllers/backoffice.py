from flask import render_template

from app import app
from app.models.tables import databaseConnection


@app.route("/bo", methods = ["GET", "POST"])
def bo():
  connect = databaseConnection("dbname='mkData3.0' user='cliente_r' host='177.184.72.6' password='Cl13nt_R'")
  database = connect.Consult("""SELECT os.codos, df.descricao_defeito, tp.descricao, os.data_abertura, cl.nome_razaosocial, cd.cidade, ba.bairro, lo.logradouro, os.num_endereco, os.operador
    FROM mk_os os
    FULL OUTER JOIN mk_os_tipo tp ON os.tipo_os = tp.codostipo
    JOIN mk_pessoas cl ON os.cliente = cl.codpessoa
    JOIN mk_os_defeitos df ON os.defeito_associado = df.coddefeito
    JOIN mk_cidades cd ON os.cd_cidade = cd.codcidade
    JOIN mk_bairros ba ON os.cd_bairro = ba.codbairro
    JOIN mk_logradouros lo ON os.cd_logradouro = lo.codlogradouro
    WHERE status='1' AND tipo_os in ('4','15','18') AND fechamento_tecnico='N' ORDER BY cd.cidade asc""")

  def dumpData(database):
    obj_list = list()
    count = 0
    for data in database:
      ob = dict()
      count += 1
      ob["column1"] = count # Quantos
      ob["column2"] = data[0] # Id
      if data[1]:
        ob["column3"] = data[1] # Defeito
      else:
        ob["column3"] = "X" # Defeito
      ob["column4"] = data[2] # Tipo
      if data[3]:
        ob["column5"] = data[3].strftime("%d/%m/%Y") # Gerada
      else:
        ob["column5"] = "X"
      ob["column6"] = data[4] # Cliente
      ob["column7"] = ""
      ob["column9"] = data[5] # Cidade
      ob["column10"] = data[6].title() # Bairro
      ob["column11"] = data[7].title() # Logradouro
      ob["column12"] = data[8] # Número
      ob["column13"] = data[9].title() # Logradouro
      obj_list.append(ob)
    return obj_list

  obj_list = dumpData(database)
  return render_template("bo.html", rows = obj_list)
