from app import db
from psycopg2 import connect
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, unique=True)
  password = db.Column(db.String)

  @property
  def is_authenticated(self):
    return True

  @property
  def is_active(self):
    return True

  @property
  def is_anonymous(self):
    return False

  def get_id(self):
    return str(self.id)

  def __init__(self, username, password):
    self.username = username
    self.password = password

  def __repr__(self):
    return "<User %r>" % self.username

class databaseConnection:
  _db = None    
  def __init__(self, conn):
    self._db = psycopg2.connect(conn)

  def consult(self, select):
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
