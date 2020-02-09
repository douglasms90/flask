from flask_wtf import FlaskForm


class dumpData():
  def dumpData(self, database, tomorrow):
    obj_list = list()
    count = 0
    for data in database:
      ob = dict()
      count += 1
      ob["column1"] = count # Quantos
      ob["column2"] = data[0] # Id
      if data[1] == 3: # Tomador
        ob["column3"] = "MULTIPLA"
      else:
        ob["column3"] = "SPEED"
      ob["column4"] = data[2] # Tipo
      if data[3]:
        ob["column5"] = data[3].strftime("%d/%m/%Y") # Gerada
      else:
        ob["column5"] = "X"
      ob["column6"] = data[4] # Cliente
      ob["column7"] = ''
      ob["column8"] = tomorrow # Distribuida
      ob["column9"] = data[5] # Cidade
      ob["column10"] = data[6].title() # Bairro
      if data[8]:
        ob["column11"] = data[8] # Defeito
      else:
        ob["column11"] = "X" # Defeito
      ob["column12"] = data[7].title() # Logradouro
      obj_list.append(ob)
    return obj_list