#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
import sys

#Database Connection
def databaseConnection():
 try:
  conn = psycopg2.connect("dbname='travapon' user='postgres' host='192.168.10.102' password='CHOFRA$ALCA*'")
  return conn
 except:
  return "Impossible to connect to the database, check your code."


def selectUsers(user,password):
 conn = databaseConnection() 
 conn.set_client_encoding('UTF8')
 cur = conn.cursor()
 cur.execute("SELECT * FROM users WHERE username=%s AND password=%s",(user,password,))
 rows = cur.fetchall()
 return rows

