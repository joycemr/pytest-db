import os
import psycopg2
from pytest import fixture

@fixture(scope="session", autouse=True)
def conn():
    DATABASE_URL = os.getenv("SQL_UNIT_TEST_DB_URL")
    conn = psycopg2.connect(DATABASE_URL)
    yield conn
    conn.close()

@fixture(scope="session", autouse=True)
def cur(conn):
    cur = conn.cursor()
    yield cur
    cur.close()

@fixture(scope='session')
def authors():
    authors = (
        ('Kurt', 'Vonnegut', 'KVonnegut@gmail.com'),
        ('Mark', 'Twain', 'MTwain@gmail.com')
    )
    return authors

@fixture(scope="function")
def setup_authors_dispose(cur, authors):
    for author in authors:
        cur.execute("select nextval('author_seq')")
        author_key = cur.fetchone()
        cur.execute('insert into author values(%s, %s, %s, %s)', author_key + author)
    yield

