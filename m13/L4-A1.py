import pandas as pd
import sqlite3

database= 'database.sqlite'

conn = sqlite3.connect(database)
print("Opened data successfully")

conn.execute("""CREATE TABLE CLASS_10
             (SNO INT PRIMARY KEY NOT NULL,
             ROLL_NO INT NOT NULL,
             NAME TEXT NOT NULL,
             AGE INT DEFAULT 15,
             GENDER TEXT NOT NULL,
             EMAIL_ID TEXT NOT NULL,
             CONTACT_NO REAL NOT NULL);""")

print("table created successfully.")

conn.execute("""INSERT INTO CLASS_10(SNO ,ROLL_NO , NAME ,AGE ,GENDER ,EMAIL_ID ,CONTACT_NO)
             VALUES (1, 1, 'Allen', 14, 'Male','allen@gmail.com',8088900);""")

conn.execute("""INSERT INTO CLASS_10(SNO ,ROLL_NO , NAME ,AGE ,GENDER ,EMAIL_ID ,CONTACT_NO)
             VALUES (2, 2, 'Aisha', 14, 'Female','aish@gmail.com',9080900);""")

conn.execute("""INSERT INTO CLASS_10(SNO ,ROLL_NO , NAME ,AGE ,GENDER ,EMAIL_ID ,CONTACT_NO)
             VALUES (3, 3, 'Jeff', 15, 'Male','allen@gmail.com',9909000);""")
conn.commit()
print("Records created successfully.")

tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type = 'table';""", conn)

print(tables)

class_10d = pd.read_sql("""SELECT *
                     FROM CLASS_10;""", conn)

print(class_10d.head())