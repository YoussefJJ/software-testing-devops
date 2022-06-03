import os
import sqlite3


def create_db():
    conn = sqlite3.connect(os.environ['DATABASE_FILENAME'])
    c = conn.cursor()
    c.execute('''CREATE TABLE users (username text, password text)''')
    c.execute('''CREATE TABLE todos (id integer primary key, title text, complete integer)''')
    conn.commit()
    conn.close()