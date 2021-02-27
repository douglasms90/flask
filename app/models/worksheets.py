from app.models.tables import db


class suporte(db):
  id = db[0]
  defeito = db[1]
  tipo = db[2]
  gerada = db[3]
	cliente = db[4]
	distribuida = db[5]
	cidade = db[6]
	bairro = db[7]
	logradouro = db[8]
	numero = db[9]
	operador = db[10]

'''
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
    ob["column8"] = tomorrow.strftime('%d/%m/%Y') # Distribuida
    ob["column9"] = data[5] # Cidade
    ob["column10"] = data[6].title() # Bairro
    ob["column11"] = data[7].title() # Logradouro
    ob["column12"] = data[8] # Número
    ob["column13"] = data[9].title() # Logradouro
    obj_list.append(ob)
  return obj_list
'''
