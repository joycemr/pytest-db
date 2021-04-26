from resources.db import cur
from pytest import fixture

# Test data setup fixtures
@fixture(scope='session')
def authors():
    authors = (
        ('Kurt', 'Vonnegut', 'KVonnegut@gmail.com'),
        ('Mark', 'Twain', 'MTwain@gmail.com')
    )
    return authors

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
def setup_authors(authors):
    for author in authors:
        cur.execute("select nextval('author_seq')")
        author_key = cur.fetchone()
        cur.execute('insert into author values(%s, %s, %s, %s)', author_key + author)
    yield


