import sqlite3 
import pandas as pd
connection = sqlite3.connect("database/retail.db")

query = "SELECT * FROM retail_sales LIMIT 10"
df =pd.read_sql(query,connection)
print(df)
connection.close()