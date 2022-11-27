#include sqlite3
import sqlite3 


connection = sqlite3.connect('database.db')


with open('db_init/schema.sql') as f:
    connection.executescript(f.read())
    
cur = connection.cursor()


cur.execute("INSERT INTO users (Username, passwords) VALUES (?, ?)", ('Vano111', '135gf'))
cur.execute("INSERT INTO users (Username, passwords) VALUES (?, ?)", ('Fedor', '77asd!'))
cur.execute("INSERT INTO users (Username, passwords) VALUES (?, ?)", ('Gena', 'hjins'))
cur.execute("INSERT INTO users (Username, passwords) VALUES (?, ?)", ('Timur', '547fg!'))
cur.execute("INSERT INTO users (Username, passwords) VALUES (?, ?)", ('Olga', 'tur45!'))


connection.commit()
connection.close()