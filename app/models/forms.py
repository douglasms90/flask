from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired
from re import match


class LoginForm(FlaskForm):
  username = StringField("username", validators=[DataRequired()])
  password = PasswordField("password", validators=[DataRequired()])

class dumpData():
  def dumpData(self, database, tomorrow):
    obj_list = list()
    count = 0
    for data in database:
      ob = dict()
      count += 1
      ob["column1"] = count # Quantos
      ob["column2"] = data[0] # Id
      ob["column3"] = data[1] # Defeito
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
      ob["column12"] = data[7].title() # Logradouro
      obj_list.append(ob)
    return obj_list