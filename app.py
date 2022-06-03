import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from Auth import addUser, checkUser, getUser

from Todo import addTodo, deleteTodo, getTodoById, getTodos, updateTodo

app = Flask(__name__)
sess = Session(app)

# /// = relative path, //// = absolute path

@app.route("/")
def home():
    if 'username' in session:
        todo_list = getTodos()
        return render_template('todo.html', username=session['username'], todo_list=todo_list)
    return render_template('login.html')

@app.route("/add", methods=["POST"])
def add():
    if 'username' in session:
        title = request.form.get("title")
        if title != "":
            addTodo(title=title, complete=False)
        return redirect(url_for("home"))
    return redirect(url_for("login"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    if 'username' in session:
        todo = getTodoById(todo_id)
        todo_as_list = list(todo)
        todo_as_list[2] = not todo_as_list[2]
        todo = tuple(todo_as_list)
        updateTodo(id=todo[0], title=todo[1], complete=todo[2])
        return redirect(url_for("home"))
    return redirect(url_for("login"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    if 'username' in session:
        deleteTodo(todo_id)
        return redirect(url_for("home"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    username = request.form.get("username")
    password = request.form.get("password")
    # check if username and password are correct
    user = checkUser(username, password)
    print(user)
    if user:
        session['username'] = username
        return redirect(url_for("home"))
    error = "Invalid credentials"
    return render_template("login.html", error=error)

@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "GET":
        return render_template("signup.html")
    print("shit")
    username = request.form.get("username")
    password = request.form.get("password")
    # check if empty username or password
    if username == "" or password == "":
        return "Invalid credentials"
    # check if username is already taken
    if getUser(username) is None:
        addUser(username, password)
        session['username'] = username
        return redirect(url_for("home"))
    # display error message
    error = "Username already taken"
    return render_template('signup.html', error=error)

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for("home"))
    
if __name__ == "__main__":
    app.secret_key = 'BAD_cxvxcvSECRET_KEY'
    app.config['SESSION_TYPE'] = 'filesystem'
    os.environ['DATABASE_FILENAME'] = 'db.sqlite'
    sess.init_app(app)
    app.run(debug=True)