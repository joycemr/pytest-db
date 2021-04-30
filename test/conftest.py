import pytest
from psycopg2.extras import NamedTupleCursor
from resources.db import conn
import resources.test_data as test_data
import resources.sql_runner as sql_runner
import resources.sql_formatter as sql_formatter


# make the connection and test data available globally without an extra import
# DB stuff
pytest.conn = conn
# pytest.cur = conn.cursor(cursor_factory=NamedTupleCursor)
# common sql runners
pytest.sql_runner = sql_runner
pytest.sql_formatter = sql_formatter
# Test data
pytest.test_data = test_data

@pytest.fixture(scope='session')
def no_data_msg():
    return 'No data returned to test'

# Test data setup pytest.fixtures
@pytest.fixture(scope='session')
def authors():
    return test_data.authors

@pytest.fixture(scope='session')
def books():
    return test_data.books

@pytest.fixture(scope="function")
def setup_authors(authors):
    for author in authors:
        with conn.cursor() as cur:
            cur.execute("select nextval('author_seq')")
            author['id'] = cur.fetchone()[0]
            sql_runner.insert('author', author)
    yield

@pytest.fixture(scope="function")
def setup_books(books):
    for book in books:
        with conn.cursor() as cur:
            cur.execute("select nextval('book_seq')")
            book['id'] = cur.fetchone()[0]
            rs = sql_runner.select('author', 'id', condition = "l_name = '" + book['l_name'] + "'")
            book['author_id'] = rs[0]
            book_params = {'id': book['id'], 'author_id': book['author_id'], 'title': book['title'], 'pub_year': book['pub_year']}
            sql_runner.insert('book', book_params)
    yield
