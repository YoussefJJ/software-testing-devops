import sqlite3
from app import app
import unittest
from unittest.mock import patch

class TestAddUser(unittest.TestCase):
    @patch("loginModule.sqlite3", spec=sqlite3)
    def test_addUser(self, mocked_object):
        # Given
        mock_execute= (mocked_object.connect.return_value.cursor.return_value.execute)
        # When
        
        # Then
        mock_execute.assert_called_once()