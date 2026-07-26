import sqlite3
import pandas as pd

def create_connection(database_name):
    connection = sqlite3.connect(database_name)

    return connection

def load_data(df,connection):
    df.to_sql(
        name ="retail_sales",
        con = connection,
        if_exists = "replace",
        index = False
    )

def close_connection(connection):
    connection.close()