import os
import db
import json
from db import cur
from pytest import fixture

# Test data setup fixtures
@fixture(scope='session')
def authors():
    authors = (
        ('Kurt', 'Vonnegut', 'KVonnegut@gmail.com'),
        ('Mark', 'Twain', 'MTwain@gmail.com')
    )
    return authors

@fixture(scope="function")
def setup_authors(authors):
    for author in authors:
        cur.execute("select nextval('author_seq')")
        author_key = cur.fetchone()
        cur.execute('insert into author values(%s, %s, %s, %s)', author_key + author)
    yield

