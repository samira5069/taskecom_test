import pandas as pd
import psycopg2 as ps
import openpyxl
import numpy as np
from sys import argv

script, file = argv
xl = pd.read_excel(file, usecols=['endpoint_id', 'endpoint_name'])
id = xl['endpoint_id'].tolist()
name = xl['endpoint_name'].tolist()
con = ps.connect(
database = "postgres",
user ="postgres",
password="123",
host="localhost",
port="5432")
cur = con.cursor()
cur.execute("""DELETE FROM endpoint_names;""")
for i in range(len(id)):
    cur.execute("""INSERT INTO endpoint_names(endpoint_id, endpoint_name) VALUES (%s,%s);""", (id[i], name[i]))
con.commit()
