import pandas as pd
import numpy as np
import sqlite3
from datetime import date

# connect to database
connection = sqlite3.connect("arkera.db")
cursor = connection.cursor()

# delete table if exists
# cursor.execute("""DROP TABLE ratings;""")

# create database
sql_command = """
 CREATE TABLE ratings (
     id integer PRIMARY KEY,
     url text NOT NULL,
     date integer NOT NULL,
     rating integer NOT NULL);"""

cursor.execute(sql_command)

# populate database
ratings = "INSERT INTO ratings(id, url, date, rating) VALUES (?, ?, ?, ?)"
cursor.execute(ratings, (1, 'http://google.com', 20170503, 5))
cursor.execute(ratings, (2, 'http://bing.com', 20100610, 2))
cursor.execute(ratings, (3, 'http://netflix.com', 20100710, 10))
cursor.execute(ratings, (4, 'http://facebook.com', 20120606, 7))

# commit database changes
connection.commit()

# pull into dataframe
sql_query = "SELECT * FROM ratings"
df = pd.read_sql(sql_query, connection)

# close database connection
connection.close()


# filter dataframe depending on results wanted.
def search(df, search):
    df_filtered = df.query(search)
    return df_filtered

# example searches

new_df = df
search1 = 'rating < 5'
search1 = search(new_df, search1)
print(search1)

search2 = 'rating < 5 | rating > 7'
search2 = search(new_df, search2)
print(search2)

search3 = ' date > 20130101'
search3 = search(new_df, search3)
print(search3)