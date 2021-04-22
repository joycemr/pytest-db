import os
import db
from pytest import fixture

# DB connection fixtures
@fixture(scope="session", autouse=True)
def conn():
    conn = db.conn
    yield conn
    conn.close()

@fixture(scope="function", autouse=True)
def cur(conn):
    cur = conn.cursor()
    yield cur
    cur.close()

# Test data setup fixtures
# @fixture(scope='session')
# def authors():
#     authors = (
#         ('Kurt', 'Vonnegut', 'KVonnegut@gmail.com'),
#         ('Mark', 'Twain', 'MTwain@gmail.com')
#     )
#     return authors

@fixture(scope='session')
def authors():
    authors = [
        {'id': None, 'f_name': 'Kurt', 'l_name': 'Vonnegut', 'email': 'KVonnegut@gmail.com'},
        {'id': None, 'f_name': 'Mark', 'l_name': 'Twain', 'email': 'MTwain@gmail.com'}
    ]
    return authors

@fixture(scope="function")
def setup_authors(cur, authors):
    for author in authors:
        cur.execute("select nextval('author_seq')")
        author['id'] = cur.fetchone()
        cur.execute('insert into author values(%(id)s, %(f_name)s, %(l_name)s, %(email)s)', list(author))
    yield

