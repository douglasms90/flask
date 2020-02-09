import psycopg2
import datetime
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

def findos(data):
 try:
  conn = psycopg2.connect("dbname='mkData3.0' user='cliente_r' host='177.184.72.6' password='Cl13nt_R'")
 except:
  return "Impossible to connect to the database, check your code."

 cur = conn.cursor()
 conn.set_client_encoding('LATIN1')
 cur.execute("SELECT os.codos ,def.descricao_defeito, p.nome_razaosocial, c.cidade, b.bairro, l.logradouro, p.numero, con.contrato, con.username, os.defeito_reclamado FROM mk_os os INNER JOIN mk_pessoas p ON os.cliente=p.codpessoa INNER JOIN mk_cidades c ON os.cd_cidade=c.codcidade INNER JOIN mk_logradouros l ON p.codlogradouro=l.codlogradouro INNER JOIN mk_bairros b ON p.codbairro=b.codbairro INNER JOIN mk_os_defeitos def ON os.defeito_associado=def.coddefeito INNER JOIN mk_conexoes con ON con.codconexao=os.conexao_associada WHERE tipo_os in (4,15) AND data_abertura=%s ORDER BY cidade ASC ,bairro ASC ,logradouro ASC ,numero ASC ",(data,)) 
 rows = cur.fetchall()
 lista = list()
 for row in rows:
  ob = dict()
  ob["ID"] = row[0]
  ob["DEFEITO"] = row[1]
  ob["CLIENTE"] = row[2]
  ob["CIDADE"] = row[3]
  ob["BAIRRO"] = row[4]
  ob["RUA"] = row[5]
  ob["NUMERO"] = row[6]
  ob["CONTRATO"] = row[7]
  ob["USERNAME"] = row[8]
  ob["PROBLEMA"] = row[9]
  lista.append(ob)
 return lista


def teste():
 try:
  conn = psycopg2.connect("dbname='mkData3.0' user='cliente_r' host='177.184.72.6' password='Cl13nt_R'")
 except:
  return "Impossible to connect to the database, check your code."

 cur = conn.cursor()
 conn.set_client_encoding('LATIN1')
 cur.execute("SELECT os.codos ,def.descricao_defeito, p.nome_razaosocial, c.cidade, b.bairro, l.logradouro, p.numero, con.contrato, con.username, os.defeito_reclamado FROM mk_os os INNER JOIN mk_pessoas p ON os.cliente=p.codpessoa INNER JOIN mk_cidades c ON os.cd_cidade=c.codcidade INNER JOIN mk_logradouros l ON p.codlogradouro=l.codlogradouro INNER JOIN mk_bairros b ON p.codbairro=b.codbairro INNER JOIN mk_os_defeitos def ON os.defeito_associado=def.coddefeito INNER JOIN mk_conexoes con ON con.codconexao=os.conexao_associada WHERE tipo_os in (4,15) AND data_abertura=current_date") 
 rows = cur.fetchall()
 lista = list()
 for row in rows:
  ob = dict()
  ob["ID"] = row[0]
  ob["DEFEITO"] = row[1]
  ob["CLIENTE"] = row[2]
  ob["CIDADE"] = row[3]
  ob["BAIRRO"] = row[4]
  ob["RUA"] = row[5]
  ob["NUMERO"] = row[6]
  ob["CONTRATO"] = row[7]
  ob["USERNAME"] = row[8]
  ob["PROBLEMA"] = row[9]
  lista.append(ob)
 return lista
