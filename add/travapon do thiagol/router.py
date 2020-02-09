# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pprint as p
import psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
import routeros_api

def databaseConnection():
 try:
  conn = psycopg2.connect("dbname='mkData3.0' user='cliente_r' host='177.184.72.6' password='Cl13nt_R'")
  return conn
 except:
  return "Impossible to connect to the database, check your code."

def procurar(user):
 #con = ['177.184.72.2','177.184.72.16','177.184.72.17','177.184.72.18','177.184.72.19','177.184.72.20','177.184.72.21','177.184.72.22','177.184.64.12','177.184.64.14','177.184.64.15']
 con = ['177.184.72.16','177.184.72.17','177.184.72.18','177.184.72.19','177.184.72.20','177.184.72.21','177.184.72.22','177.184.64.12','177.184.64.14','177.184.64.15']
 for i in con:
  connection = routeros_api.RouterOsApiPool(i, username='suporte', password='123')
  api = connection.get_api()
  ppp = api.get_resource('/ppp/active').get(name=user)
  if ppp:
   status = 'Conectado'
   break  
   connection.disconnect()    
  else:   
   status = 'Nao conectado'
   connection.disconnect()
 return status  


def getUser(user):
 conn = databaseConnection()
 cur = conn.cursor()
 conn.set_client_encoding('LATIN1')
 if user.isdigit(): 
  contrato = cur.execute("SELECT p.nome_razaosocial, b.bairro, l.logradouro, p.numero, c.username, c.contrato FROM mk_conexoes c INNER JOIN mk_pessoas p ON c.codcliente=p.codpessoa INNER JOIN mk_bairros b ON b.codbairro=p.codbairro INNER JOIN mk_logradouros l ON l.codlogradouro=p.codlogradouro WHERE contrato=%s",(user,))
  contrato = cur.fetchall()
  if contrato: 
   status = procurar(contrato[0][4])
   contrato.append(status)
   return contrato
  return 'Nao ha registros' 
 else:
  usuario = cur.execute("SELECT p.nome_razaosocial, b.bairro, l.logradouro, p.numero, c.username, c.contrato FROM mk_conexoes c INNER JOIN mk_pessoas p ON c.codcliente=p.codpessoa INNER JOIN mk_bairros b ON b.codbairro=p.codbairro INNER JOIN mk_logradouros l ON l.codlogradouro=p.codlogradouro WHERE username=%s",(user,))
  usuario = cur.fetchall()
  if usuario:
   status = procurar(user)
   usuario.append(status)
   return usuario
  return 'Nao ha registros'




