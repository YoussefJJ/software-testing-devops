import os
import sqlite3


def addUser(username,password):
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    cur = connection.cursor()
    cur.execute("INSERT INTO User(USERNAME,PASSWORD) VALUES(?, ?)", (username, password))
    connection.commit()

def getUser(username):
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    cur = connection.cursor()
    cur.execute("SELECT * FROM User WHERE USERNAME=?", (username,))
    user = cur.fetchone()
    connection.close()
    return user

def checkUserCredentials(username,password):
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    cur = connection.cursor()
    cur.execute("SELECT * FROM User WHERE USERNAME=? AND PASSWORD=?", (username,password))
    user = cur.fetchone()
    connection.close()
    if user:
        return True
    else:
        return False

def checkUserExists(username):
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    cur = connection.cursor()
    cur.execute("SELECT * FROM User WHERE USERNAME=?", (username,))
    user = cur.fetchone()
    connection.close()
    if user:
        return True
    else:
        return False