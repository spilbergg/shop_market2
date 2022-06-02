
import sqlite3

connect = sqlite3.connect('db.sqlite3')
cursor = connect.cursor()
cursor.execute('SELECT * FROM market_30_product')
print(cursor.fetchall())

cursor.close()