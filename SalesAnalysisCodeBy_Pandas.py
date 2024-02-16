import pandas as pd
from sqlalchemy import create_engine

# Database connection parameters
username = 'root'
password = 'sam123'
hostname = 'localhost'
database_name = 'mydb'

engine_str = f'mysql+mysqlconnector://{username}:{password}@{hostname}/{database_name}'
engine = create_engine(engine_str)


df_sales = pd.read_sql_query("SELECT * FROM Sales", engine)
df_order = pd.read_sql_query("SELECT * FROM `Order`", engine)
df_customer = pd.read_sql_query("SELECT * FROM Customer", engine)
df_items = pd.read_sql_query("SELECT * FROM Items", engine)

df = pd.merge(df_order, df_sales, on='sales_id')
df = pd.merge(df, df_customer, on='customer_id')
df = pd.merge(df, df_items, on='item_id')

df_filtered = df[(df['age'] >= 18) & (df['age'] <= 35) & (df['quantity'] > 0)]

df_grouped = df_filtered.groupby(['customer_id', 'age', 'item_name'])['quantity'].sum().reset_index()

df_grouped.rename(columns={'customer_id': 'Customer', 'item_name': 'Item', 'quantity': 'Quantity'}, inplace=True)


df_grouped.to_csv('salesAnalysis.csv', index=False, sep=';')
