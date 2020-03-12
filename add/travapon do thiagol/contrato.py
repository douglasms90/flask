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

def getContrato(user):
 conn = databaseConnection()
 cur = conn.cursor()
 conn.set_client_encoding('LATIN1')
 resultado = cur.execute("SELECT p.nome_razaosocial, cd.cidade, b.bairro, l.logradouro,p.numero, c.cancelado, c.codcontrato FROM mk_contratos c INNER JOIN mk_pessoas p ON p.codpessoa=c.cliente INNER JOIN mk_bairros b ON b.codbairro=p.codbairro INNER JOIN mk_cidades cd ON cd.codcidade=p.codcidade INNER JOIN mk_logradouros l ON l.codlogradouro=p.codlogradouro LEFT JOIN mk_conexoes ct ON ct.codcliente=p.codpessoa WHERE codcontrato=%s",(user,)) 
 resultado = cur.fetchall()
 return resultado

def checkConection(user):
 conn = databaseConnection()
 cur = conn.cursor()
 conn.set_client_encoding('LATIN1')
 resultado = cur.execute("SELECT username FROM mk_conexoes WHERE contrato=%s",(user,))
 resultado = cur.fetchall()
 ob = {}
 for i in resultado:
  ob['username'] = i[0]
 #con = ['177.184.72.2','177.184.72.16','177.184.72.17','177.184.72.18','177.184.72.19','177.184.72.20','177.184.72.21','177.184.64.12','177.184.64.14','177.184.64.15']
 con = ['177.184.72.16','177.184.72.17','177.184.72.18','177.184.72.19','177.184.72.20','177.184.72.21','177.184.64.12','177.184.64.14','177.184.64.15']
 for i in con:
  connection = routeros_api.RouterOsApiPool(i, username='suporte', password='123')
  api = connection.get_api()
  ppp = api.get_resource('/ppp/active').get(name=ob['username'])
  if ppp:
   status = 'Connected'
   break  
   connection.disconnect()    
  else:   
   status = 'Disconnected'
   connection.disconnect()
 return status  







