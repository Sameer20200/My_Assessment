import sqlite3
import csv
import pandas as pd


conn = sqlite3.connect('Data Engineer Assignment.db')
cursor = conn.cursor()

df_sales = pd.read_sql_query("SELECT * FROM Sales", conn)
df_order = pd.read_sql_query("SELECT * FROM `Orders`", conn)
df_customer = pd.read_sql_query("SELECT * FROM Customers", conn)
df_items = pd.read_sql_query("SELECT * FROM Items", conn)

df = pd.merge(df_order, df_sales, on='sales_id')
df = pd.merge(df, df_customer, on='customer_id')
df = pd.merge(df, df_items, on='item_id')

df_filtered = df[(df['age'] >= 18) & (df['age'] <= 35) & (df['quantity'] > 0)]

df_grouped = df_filtered.groupby(['customer_id', 'age', 'item_name'])['quantity'].sum().reset_index()

df_grouped.rename(columns={'customer_id': 'Customer', 'item_name': 'Item', 'quantity': 'Quantity'}, inplace=True)

df_grouped.to_csv('Analysis_pandas.csv', index=False, sep=';')

conn.close()
