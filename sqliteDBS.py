import sqlite3

def createTable():
    connect=sqlite3.connect('lite.db')
    cursor=connect.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER,price REAL)')
    connect.commit()
    connect.close()

def insert(item,quantity,price):
    connect=sqlite3.connect('lite.db')
    cursor=connect.cursor()
    cursor.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    connect.commit()
    connect.close()

def view():
    connect=sqllite3.connect('lite.db')
    cursor=connect.cursor()
    cursor.execute('SELECT*FROM store')
    rows=cursor.fetchall()
    connect.close()
    return rows

print(view())
insert('water glass',10,5)