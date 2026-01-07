import pandas as pd
import sqlite3

database= 'database.sqlite'

conn = sqlite3.connect(database)
print("Opened data successfully")

tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type = 'table';""", conn)

print("All tables in the database: ")
print(tables)

team = pd.read_sql("""SELECT * FROM Team;""", conn)

print("\nTeam Table (first five rows):")
print(team.head())

matches = pd.read_sql("""SELECT * FROM Match;""", conn)
