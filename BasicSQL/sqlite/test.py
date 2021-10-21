import sqlite3
con = sqlite3.connect('chinook.db')

cur = con.cursor()

#cur.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')

#cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
t = ('RHAT',)
cur.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(cur.fetchone())


con.commit()

con.close()