from app.models.tables import db

class dumpdata:
	def support(db, tomorrow):
		obj_list = list()
		count = 0
		for data in db:
			ob = dict()
			count += 1
			ob["QUANTOS"] = count
			ob["ID"] = data[0]
			if data[1]:
				ob["DEFEITO"] = data[1]
			else:
				ob["DEFEITO"] = "X"
			ob["TIPO"] = data[2]
			if data[3]:
				ob["GERADA"] = data[3].strftime("%d/%m/%Y")
			else:
				ob["GERADA"] = "X"
			ob["CLIENTE"] = data[4]
			ob["NULL"] = ""
			ob["DISTRIBUIDA"] = tomorrow.strftime('%d/%m/%Y')
			ob["CIDADE"] = data[5]
			ob["BAIRRO"] = data[6].title()
			ob["LOGRADOURO"] = data[7].title()
			ob["NUMERO"] = data[8]
			ob["OPERADOR"] = data[9].title()
			obj_list.append(ob.values())
		return obj_list

	def backoffice(db, tomorrow):
		obj_list = list()
		count = 0
		for data in db:
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

