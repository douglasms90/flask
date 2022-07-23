from psycopg2 import connect
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


class dbConn():
  conn = None
  def __init__(self):
    self.conn = psycopg2.connect("dbname='' user='' host='' password=''")

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
