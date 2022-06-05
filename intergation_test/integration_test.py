import os
import sys
from app import create_app
sys.path.append( '../flask-todo' )

from db_initialize import create_db
import pytest



@pytest.fixture(scope="session", autouse=True)
def create_test_database(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp("tmp")
    database_filename = tmp_dir / "db.sqlite"
    create_db(database_filename)
    os.environ['DATABASE_FILENAME'] = str(database_filename)

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(__name__,test=True)
    flask_app.secret_key = 'youssef'
    flask_app.config.update({"TESTING":True,})
    testing_client = flask_app.test_client(use_cookies=True)
    context = flask_app.app_context()
    context.push()
    yield testing_client
    context.pop()

def test_home(test_client):
    # Given
    expected_status_code = 200
    expected_title = "Todo App"
    # When
    response = test_client.get("/")
    # Then
    assert response.status_code == 200
    assert expected_title in response.data.decode("utf-8")

def test_signup(test_client):
    # Given
    expected_status_code = 200
    expected_title = "Sign Up"
    # When
    response = test_client.get("/signup")
    # Then
    assert response.status_code == 200
    assert expected_title in response.data.decode("utf-8")

def test_login(test_client):
    # Given
    expected_status_code = 200
    expected_title = "Log-in to your account"
    # When
    response = test_client.get("/login")
    # Then
    assert response.status_code == 200
    assert expected_title in response.data.decode("utf-8")

def test_login_post_success(test_client):
    # Given
    expected_status_code = 200
    expected_title = "Todo App"
    data = {
        "username": "youssefjj",
        "password": "123"
    }
    # When
    response = test_client.post("/login", data=data, follow_redirects=True)
    # Then
    assert response.status_code == expected_status_code
    assert expected_title in response.data.decode("utf-8")

def test_login_post_failure(test_client):
    # Given
    expected_status_code = 200
    expected_error_message = "Invalid credentials"
    data = {
        "username": "test",
        "password": "1234"
    }
    # When
    response = test_client.post("/login", data=data, follow_redirects=True)
    # Then
    assert response.status_code == expected_status_code
    assert expected_error_message in response.data.decode("utf-8")

def test_signup_post_success(test_client):
    # Given
    expected_status_code = 200
    expected_title = "Todo App"
    data = {
        "username": "youssefjj",
        "password": "123"
    }
    # When
    response = test_client.post("/signup", data=data, follow_redirects=True)
    # Then
    assert response.status_code == expected_status_code
    assert expected_title in response.data.decode("utf-8")

def test_signup_post_failure(test_client):
    # Given
    expected_status_code = 200
    expected_error_message = "Username already taken"
    data = {
        "username": "youssefjj",
        "password": "abcd"
    }
    # When
    response = test_client.post("/signup", data=data, follow_redirects=True)
    # Then
    assert response.status_code == expected_status_code
    assert expected_error_message in response.data.decode("utf-8")

def test_logout(test_client):
    # Given
    expected_status_code = 200
    expected_title = "Log-in to your account"
    # When
    response = test_client.get("/logout", follow_redirects=True)
    # Then
    assert response.status_code == expected_status_code
    assert expected_title in response.data.decode("utf-8")

def test_todo_list(test_client):
    # Given
    expected_status_code = 200
    with test_client.session_transaction() as session:
        session['username'] = "youssef"
    expected_content = '''<p class="ui big header">1 | test</p>'''
    expected_content2 = '''<p class="ui big header">2 | test2</p>'''
    # When
    response = test_client.get("/", follow_redirects=True)
    # Then
    assert response.status_code == expected_status_code
    assert expected_content in response.data.decode("utf-8")
    assert expected_content2 in response.data.decode("utf-8")

def test_add_todo(test_client):
    # Given
    expected_status_code = 200
    expected_completion_text = "testing"
    with test_client.session_transaction() as session:
        session['username'] = "youssef"
    data = {
        "title": "testing"
    }
    # When
    response = test_client.post("/add", data=data, follow_redirects=True)
    # Then
    assert response.status_code == expected_status_code
    assert expected_completion_text in response.data.decode("utf-8")

def test_unauthorized_add_todo(test_client):
    # Given
    expected_status_code = 200
    with test_client.session_transaction() as session:
        session.clear()
    expected_title = "Log-in to your account"
    data = {
        "title": "testing"
    }
    # When
    response = test_client.post("/add", data=data, follow_redirects=True)
    # Then
    assert response.status_code == expected_status_code
    assert expected_title in response.data.decode("utf-8")

def test_update_todo(test_client):
    # Given
    expected_status_code = 200
    expected_completion_text = '''<span id="state" class="ui green label">Completed</span>'''
    with test_client.session_transaction() as session:
        session['username'] = "youssef"
    # When
    response = test_client.get("/update/1", follow_redirects=True)
    # Then
    assert response.status_code == expected_status_code
    assert expected_completion_text in response.data.decode("utf-8")

def test_unauthorized_update_todo(test_client):
    # Given
    with test_client.session_transaction() as session:
        session.clear()
    expected_status_code = 200
    expected_title = "Log-in to your account"
    data = {
        "title": "testing"
    }
    # When
    response = test_client.get("/update/1", data=data, follow_redirects=True)
    # Then
    assert response.status_code == expected_status_code
    assert expected_title in response.data.decode("utf-8")

def test_delete_todo(test_client):
    # Given
    expected_status_code = 200
    expected_completion_text = '''<p class="ui big header">1 | test</p>'''
    with test_client.session_transaction() as session:
        session['username'] = "youssef"

    data = {
        "title": "updated title with id 1"
    }
    # When
    response = test_client.get("/delete/1", data=data, follow_redirects=True)
    # Then
    assert response.status_code == expected_status_code
    assert expected_completion_text not in response.data.decode("utf-8")

def test_unauthenticated_delete_todo(test_client):
    # Given
    expected_status_code = 200
    with test_client.session_transaction() as session:
        session.clear()
    expected_title = "Log-in to your account"
    data = {
        "title": "testing"
    }
    # When
    response = test_client.get("/delete/1", data=data, follow_redirects=True)
    # Then
    assert response.status_code == expected_status_code
    assert expected_title in response.data.decode("utf-8")
