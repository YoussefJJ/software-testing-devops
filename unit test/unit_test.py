import os
import sqlite3
import sys
sys.path.append( '../flask-todo' )

from Auth import addUser, checkUserCredentials, checkUserExists, getUser
import unittest
from unittest.mock import Mock, patch

from Todo import addTodo, deleteTodo, getTodoById, getTodos, updateTodo


os.environ['DATABASE_FILENAME'] = 'db.sqlite'


class TestAddUser(unittest.TestCase):
    @patch("Auth.sqlite3", spec=sqlite3)
    def test_addUser(self, mocked_object):
        # Given
        mock_execute= (mocked_object.connect.return_value.cursor.return_value.execute)
        # When
        addUser('test','test')
        # Then
        mock_execute.assert_called_once()
    
class CheckUser(unittest.TestCase):
    def test_check_user_credentials(self):
        # Given
        username = 'youssef'
        password = '123'
        expected = True
        # When
        result = checkUserCredentials(username, password)
        # Then
        self.assertEqual(result, expected)
    def test_check_user_exists(self):
        #Given
        username = 'youssefjj'
        expected = True
        #When
        result = checkUserExists(username)
        #Then
        self.assertEqual(result, expected)

class GetUser(unittest.TestCase):
    def test_get_user(self):
        # Given
        username = 'youssef'
        expected = ('youssef', '123')
        # When
        result = getUser(username)
        # Then
        self.assertEqual(result, expected)

class GetTodos(unittest.TestCase):
    @patch('Todo.sqlite3')
    def test_get_inexistant_todo(self, mocked_object):
        # Given
        mocked_object.connect().cursor().fetchone.return_value = None
        expected_value = None
        # When
        result = getTodoById(1)
        # Then
        self.assertEqual(result, expected_value)
    
    @patch('Todo.sqlite3')
    def test_get_todo(self, mocked_object):
        # Given
        mocked_object.connect().cursor().fetchone.return_value = (2, 'test', 1)
        expected_value = (2, 'test', 1)
        # When
        result = getTodoById(1)
        # Then
        self.assertEqual(result, expected_value)
    
    @patch('Todo.sqlite3')
    def test_get_todos(self, mocked_object):
        # Given
        mocked_object.connect().cursor().fetchall.return_value = [(1, 'test', 1), (2, 'test', 1)]
        expected_value = [(1, 'test', 1), (2, 'test', 1)]
        # When
        result = getTodos()
        # Then
        self.assertEqual(result, expected_value)

class TestAddTodo(unittest.TestCase):
    @patch('Todo.sqlite3', spec=sqlite3)
    def test_add_todo(self, mocked_object):
        # Given
        mock_execute=(mocked_object.connect.return_value.cursor.return_value.execute)
        # When
        addTodo('test')
        # Then
        mock_execute.assert_called_once()

class TestUpdateTodo(unittest.TestCase):
    @patch('Todo.sqlite3', spec=sqlite3)
    def test_update_todo(self, mocked_object):
        # Given
        mock_execute=(mocked_object.connect.return_value.cursor.return_value.execute)
        # When
        updateTodo(1,'test', True)
        # Then
        mock_execute.assert_called_once()

class TestDeleteTodo(unittest.TestCase):
    @patch('Todo.sqlite3', spec=sqlite3)
    def test_delete_todo(self, mocked_object):
        # Given
        mock_execute=(mocked_object.connect.return_value.cursor.return_value.execute)
        # When
        deleteTodo(1)
        # Then
        mock_execute.assert_called_once()