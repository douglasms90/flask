from psycopg2 import connect
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


class dbc():
    conn = None
    def __init__(self, host):
        self.conn = psycopg2.connect(host)

    def consult(self, query):
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            dump = cur.fetchall()
            return dump
        except:
            return "Impossible to connect to the database, check your code."

    def close(self):
        self.conn.close()
