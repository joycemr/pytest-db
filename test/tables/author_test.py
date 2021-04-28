from pytest import mark
from resources.sql_runner import select
from resources.result_formatter import get_first_row
from resources.db import conn
from psycopg2.extras import NamedTupleCursor


@mark.authors
@mark.tables
class TestAuthors:

    @mark.parametrize('expected', [
        {'f_name': 'Kurt', 'l_name': 'Vonnegut', 'email': 'KVonnegut@gmail.com'},
        {'f_name': 'Mark', 'l_name': 'Twain', 'email': 'MTwain@gmail.com'}
    ])
    def test_Authors(self, setup_authors, expected):
        with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            sql = 'select * from author where l_name = %s'
            cur.execute(sql, (expected['l_name'],))
            rs = cur.fetchall()
            actual = get_first_row(rs)
        assert actual.f_name == expected['f_name']
        assert actual.l_name == expected['l_name']
        assert actual.email == expected['email']

    def test_Vonnegut(self, setup_authors):
        rs = select('author', '*', condition = "l_name = 'Vonnegut'")
        actual = get_first_row(rs)
        assert actual.f_name == 'Kurt'
        assert actual.l_name == 'Vonnegut'
        assert actual.email == 'KVonnegut@gmail.com'

    def test_Twain(self, setup_authors):
        rs = select('author', '*', condition = "l_name = 'Twain'")
        actual = get_first_row(rs)
        print(actual)
        assert actual.f_name == 'Mark'
        assert actual.l_name == 'Twain'
        assert actual.email == 'MTwain@gmail.com'
