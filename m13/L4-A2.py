import pandas as pd
import sqlite3

database= 'database.sqlite'

conn = sqlite3.connect(database)
print("Opened data successfully")

df = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type = 'table';""", conn)

print(df)

player_match = pd.read_sql("""SELECT *
                     FROM Player_Match;""", conn)

print(player_match.head())

null_player_match = pd.read_sql("""SELECT *
                     FROM Player_Match
                     WHERE Team_Id IS NULL;""", conn)

print(null_player_match)

toss_desc = pd.read_sql("""SELECT *
                     FROM Match;""", conn)

print(toss_desc.head())

null_match = pd.read_sql("""SELECT *
                     FROM Match
                     WHERE Match_Winner IS NULL;""", conn)

print(null_match)