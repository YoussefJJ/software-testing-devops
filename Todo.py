# get todo from sqlite
import os
import sqlite3


def getTodos():
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    cur = connection.cursor()
    cur.execute("SELECT * FROM Todo")
    todos = cur.fetchall()
    connection.close()
    print(todos)
    return todos
    
def addTodo(title, complete=False):
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    cur = connection.cursor()
    cur.execute("INSERT INTO Todo(TITLE,COMPLETE) VALUES(?, ?)", (title, complete))
    connection.commit()
    connection.close()

def getTodoById(id):
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    cur = connection.cursor()
    cur.execute("SELECT * FROM Todo WHERE ID=?", (id,))
    todo = cur.fetchone()
    connection.close()
    return todo

def updateTodo(id, title, complete):
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    cur = connection.cursor()
    cur.execute("UPDATE Todo SET TITLE=?, COMPLETE=? WHERE ID=?", (title, complete, id))
    connection.commit()
    connection.close()

def deleteTodo(id):
    database_filename = os.environ.get('DATABASE_FILENAME')
    connection = sqlite3.connect(database_filename, check_same_thread=False)
    cur = connection.cursor()
    cur.execute("DELETE FROM Todo WHERE ID=?", (id,))
    connection.commit()
    connection.close()