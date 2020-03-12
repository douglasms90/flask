# -*- coding: utf-8 -*-
import datetime
from termcolor import colored
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import re
import json
import pprint as p
import psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
import routeros_api


def procurar(user):
 con = ['177.184.72.2','177.184.72.16','177.184.72.17','177.184.72.18','177.184.72.19','177.184.72.20','177.184.72.21','177.184.72.22','177.184.64.12','177.184.64.14','177.184.64.15']
 for i in con:
  connection = routeros_api.RouterOsApiPool(i, username='suporte', password='123')
  api = connection.get_api()
  ppp = api.get_resource('/ppp/active').get(name=user)
  if ppp:
   status = False
   break  
   connection.disconnect()    
  else:   
   status = True
   connection.disconnect()
 return status  

def databaseConnection():
 try:
  conn = psycopg2.connect("dbname='mkData3.0' user='cliente_r' host='177.184.72.6' password='Cl13nt_R'")
  return conn
 except:
  return "Impossible to connect to the database, check your code."

def getUser(user):
 conn = databaseConnection()
 cur = conn.cursor()
 conn.set_client_encoding('LATIN1')
 rows = cur.execute("SELECT p.nome_razaosocial, b.bairro, l.logradouro, p.numero, c.username, c.contrato FROM mk_conexoes c INNER JOIN mk_pessoas p ON c.codcliente=p.codpessoa INNER JOIN mk_bairros b ON b.codbairro=p.codbairro INNER JOIN mk_logradouros l ON l.codlogradouro=p.codlogradouro WHERE username=%s ORDER BY bairro ASC, logradouro ASC, numero ASC ",(user,))
 rows = cur.fetchall()
 return rows

def getFiles():
 currentDay = datetime.datetime.now()
 numdays = 2
 dateList = []
 for x in range (0, numdays):
  date = currentDay - datetime.timedelta(days = x)
  days = date.strftime("%d.%m.%Y")
  dateList.append(days)

 path = "/var/log/mikrotik/"

 files = [filename for root, dirs, files in os.walk(path)
          for filename in files
          for date in dateList
          if filename.endswith(date+".log")]
 return sorted(files)


def read():
  files = getFiles()
  count = 0
  w = open("LOGS.log","w").close()
  w = open("LOGS.log","a")
  while (count<len(files)):
   for i in files:
    r = open("/var/log/mikrotik/"+i,"r")
    for line in r:
     w.write(line)
     count += 1
   w.close()

  f = open('LOGS.log', 'r')
  log = dict()
  for line in f:
      reg = re.search(r': ((?:dis)?connected)', line)  # finds connected or disconnected
      if reg is not None:
          user = re.search(r'<pppoe-(.*?)>', line).group(1)
          # if the user in the log, get it, else create it with empty dict
          ob = log.setdefault(user, dict({'USER': user}))
          ob['CONNECTION'] = reg.group(1)
          time = re.search(r'^\w{3}\s{1,2}\d{1,2}\s(?:\d{2}:){2}\d{2}', line).group(0)
          if ob['CONNECTION'].startswith('dis'):
              ob['END'] = time
          else:
              ob['START'] = time
              if 'END' in ob:
                  ob.pop('END')
  return log

def main():
 start = time.time()
 log = read()
 dic = []
 for i in log.itervalues():
  if i['CONNECTION'] == 'disconnected':
   username = i['USER']
   users = getUser(username)
   for u in users:
    ob = {}
    ob["CLIENTE"] = u[0]
    ob["BAIRRO"] = u[1]
    ob["RUA"] = u[2]
    ob["NUMERO"] = u[3]
    ob["USERNAME"] = u[4]
    ob["CONTRATO"]= u[5]
    ob["HORARIO"] = i["END"]
    dic.append(ob)

 return dic

def checkAgain():
 log = read()
 dic = []
 for i in log.itervalues():
  if i['CONNECTION'] == 'disconnected':
   username = i['USER']
   status = procurar(username)
   if status== True:
    users = getUser(username)
    for u in users:
     ob = {}
     ob["CLIENTE"] = u[0]
     ob["BAIRRO"] = u[1]
     ob["RUA"] = u[2]
     ob["NUMERO"] = u[3]
     ob["USERNAME"] = u[4]
     ob["CONTRATO"]= u[5]
     ob["HORARIO"] = i["END"]
     dic.append(ob)

 return dic


if __name__ == "__main__":
 main()    