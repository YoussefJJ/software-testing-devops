import os
import sys
sys.path.append( '../flask-todo' )

from db_initialize import create_db
import pytest



@pytest.fixture(scope="session", autouse=True)
def create_test_database(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp("tmp")
    database_filename = tmp_dir / "db.sqlite.db"
    create_db(database_filename)
    os.environ['DATABASE_FILENAME'] = str(database_filename)