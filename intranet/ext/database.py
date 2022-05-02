from psycopg2 import connect
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


def init_app(app):
  db = None    
  def __init__(self):
    self.db = psycopg2.connect("dbname='' user='' host='' password=''")

  def consult(self, select):
    db = None 
    try:
      cur = self.db.cursor()
      cur.execute(select)
      db = cur.fetchall()
      return db
    except:
      return "Impossible to connect to the database, check your code."
  
  def close(self):
    self.db.close()
