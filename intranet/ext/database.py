from flask_sqlalchemy import SQLAlchemy

from psycopg2 import connect
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
