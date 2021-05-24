import pytest
import csv
from psycopg2.extras import NamedTupleCursor
from resources.db import conn
import resources.sql_runner as sql_runner
import resources.sql_formatter as sql_formatter

author_csv = 'test/data/author.csv'
book_csv = 'test/data/book.csv'

# make the connection and test data available globally without an explicit import
# by setting additional varables in the pytest object

# DB stuff
pytest.conn = conn
# common sql runners
pytest.sql_runner = sql_runner
pytest.sql_formatter = sql_formatter
# Test data
    # it would seem that you could use the authors and books fixtures for the expected test data,
    # however, a fixture cannot be used in the parameterize decorator, so we need to expose these
    # dictionaries globally as well
pytest.authors = csv.DictReader(open(author_csv));
pytest.books = csv.DictReader(open(book_csv))

# just a little common error message
@pytest.fixture(scope='session')
def no_data_msg():
    return 'No data returned to test'

# Test data fixtures
@pytest.fixture(scope='session')
def authors():
    return csv.DictReader(open(author_csv))

@pytest.fixture(scope='session')
def books():
    return csv.DictReader(open(book_csv))

# This fixture sets up all the test data each time a
# function is ran. Since psychopg2 runs on implicit commit
# there is no need to clean up after each run
@pytest.fixture(scope="function")
def setup_data(authors, books):
    for author in authors:
        sql_runner.insert('author', author)
    for book in books:
        sql_runner.insert('book', book)

