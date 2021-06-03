import sqlite3
conn=sqlite3.connect('virat.db')
db=conn.cursor()
db.execute('''CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)''')
db.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit()
for row in db.execute('SELECT * FROM stocks'):
	print(row)
conn.close()