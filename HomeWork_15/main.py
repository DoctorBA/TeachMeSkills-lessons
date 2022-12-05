'''Задача 1.
Создать приложение, которое будет выводить на веб-страницу данные с таблицы
из базы данных. 
Столбцы таблицы:
    -Username
    -password
    -registration_date
'''
#include flask
from flask import Flask, render_template 
#include sqlite3
import sqlite3


def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


app = Flask(__name__)


@app.route('/')
def index():
    connetion = get_db_connection()
    users = connetion.execute('SELECT * FROM users').fetchall()
    connetion.close()
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True) 