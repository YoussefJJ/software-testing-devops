import os
import sqlite3


def create_db(database_filename):
    conn = sqlite3.connect(database_filename)
    c = conn.cursor()
    c.execute('''CREATE TABLE user (username text, password text)''')
    c.execute('''CREATE TABLE todo (id integer primary key, title text, complete integer)''')
    c.execute('''INSERT INTO user values ('youssef', '123'), ('test', 'test') ''')
    c.execute('''INSERT INTO todo values (1, 'test', 0), (2, 'test2', 0) ''')
    conn.commit()
    conn.close()