import sqlite3
import csv

conn = sqlite3.connect('Data Engineer Assignment.db')
cursor = conn.cursor()

query = """
SELECT S.customer_id AS Customers,C.age AS Age, I.item_name AS Item,SUM(O.quantity) AS Quantity
FROM Orders O
JOIN Sales S ON O.sales_id = S.sales_id
JOIN Customers C ON S.customer_id = C.customer_id
JOIN Items I ON O.item_id = I.item_id
WHERE C.age BETWEEN 18 AND 35 AND O.quantity > 0
GROUP BY S.customer_id, C.age, I.item_name
HAVING SUM(O.quantity) > 0
ORDER BY  S.customer_id, I.item_name;
"""

cursor.execute(query)
rows = cursor.fetchall()

with open('Sales_Analysis_Solution.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Customer', 'Age', 'Item', 'Quantity'])  # write the header
    writer.writerows(rows)

conn.close()
