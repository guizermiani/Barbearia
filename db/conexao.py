import psycopg2
import os

def conecta_db():
    database_url = os.getenv("DATABASE_URL")
    con = psycopg2.connect(database_url)
    return con



#def conecta_db():
#   con =  psycopg2.connect(host="127.0.0.1",
#                    database="postgres",
#                    user='postgres',
#                    password="10042009",
#                    port=5432)
#   return con

   