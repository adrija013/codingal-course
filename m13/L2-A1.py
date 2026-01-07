import pandas as pd
import sqlite3

database= 'database.db'

conn = sqlite3.connect(database)
print("Opened data successfully")

tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type = 'table';""", conn)

print(tables)
print("--------------")

df = pd.read_sql("""SELECT * FROM salesman;""", conn)
print(df)
print("--------------")

df1 = pd.read_sql("""SELECT * FROM salesman
                  WHERE city LIKE '%e';""", conn)
print(df1)
print("--------------")

print(df1.dtypes)
print(df1.columns)
print("--------------")

df2 = pd.read_sql("""SELECT SUM(Comission) as total_comission FROM salesman
                  WHERE Comission > 0.12;""", conn)
print(df2)