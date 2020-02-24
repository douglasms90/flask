from psycopg2 import connect
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


class databaseConnection:
  _db = None    
  def __init__(self, conn):
    self._db = psycopg2.connect(conn)

  def Consult(self, select):
    database = None 
    try:
      cur = self._db.cursor()
      cur.execute(select)
      database = cur.fetchall()
      return database
    except:
      return "Impossible to connect to the database, check your code."
  
  def close(self):
    self._db.close()