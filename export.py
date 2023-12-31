from fastapi import FastAPI
import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM Users')

users = cursor.fetchall()

connection.commit()
connection.close()

app = FastAPI()

@app.get('/')
def root():
    return users