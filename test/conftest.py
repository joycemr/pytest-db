from resources.db import conn
from pytest import fixture

# Test data setup fixtures
@fixture(scope='session')
def authors():
    authors = [
        {'f_name': 'Kurt', 'l_name': 'Vonnegut', 'email': 'KVonnegut@gmail.com'},
        {'f_name': 'Mark', 'l_name': 'Twain', 'email': 'MTwain@gmail.com'}
    ]
    return authors

@fixture(scope='session')
def authors_tuples(authors):
    return [(d['f_name'], d['l_name'], d['email']) for d in authors]

@fixture(scope='session')
def books_twain():
    books_twain = (
        ('The Adventures Of Tom Sawyer', '1876'),
        ('The Adventures of Huckleberry Finn', '1885'),
        ("A Connecticut Yankee in King Arthur's Court", '1889'),
        ('Letters from the Earth', '1962'),
    )
    return books_twain

@fixture(scope='session')
def books_vonnegut():
    books_vonnegut = (
        ('Slaughterhouse-Five', '1969'),
        ('The Sirens of Titan', '1959'),
        ("Cat's Cradle", '1963'),
        ('Player Piano', '1952'),
    )
    return books_vonnegut

@fixture(scope="function")
def setup_authors(authors_tuples):
    for author in authors_tuples:
        with conn.cursor() as cur:
            cur.execute("select nextval('author_seq')")
            author_key = cur.fetchone()
            cur.execute('insert into author values(%s, %s, %s, %s)', author_key + author)
    yield


