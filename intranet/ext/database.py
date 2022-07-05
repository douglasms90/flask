from psycopg2 import connect
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


class dbConn():
  conn = None
  def __init__(self):
    self.conn = psycopg2.connect("")

  def consult(self, query):
    try:
      cur = self.conn.cursor()
      cur.execute(query)
      dbdump = cur.fetchall()
      return dbdump
    except:
      return "Impossible to connect to the database, check your code."
    
  def close(self):
    self.conn.close()

'''
def init_app(app):
  conn = psycopg2.connect("dbname='mkData3.0' user='cliente_r' host='177.184.72.6' password='Cl13nt_R'")

  try:
    cur = conn.cursor()
    cur.execute(select)
    db = cur.fetchall()
    return db
  except:
    return "Impossible to connect to the database, check your code."
'''