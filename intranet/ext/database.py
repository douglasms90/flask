from flask_sqlalchemy import SQLAlchemy

from psycopg2 import connect
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


class dbc():
    db_ = None
    def __init__(self, host):
        self.db_ = psycopg2.connect(host)

    def consult(self, query):
        try:
            cur = self.db_.cursor()
            cur.execute(query)
            dump = cur.fetchall()
            return dump
        except:
            return "Impossible to connect to the database, check your code."

    def close(self):
        self.db_.close()

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
