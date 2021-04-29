import pytest
from psycopg2.extras import NamedTupleCursor


@pytest.mark.authors
@pytest.mark.tables
class TestAuthors:

    def test_Vonnegut(self, setup_authors):
        rs = pytest.sql_runner.select('author', '*', condition = "l_name = 'Vonnegut'")
        actual = pytest.result_formatter.get_first_row(rs)
        assert actual.f_name == 'Kurt'
        assert actual.l_name == 'Vonnegut'
        assert actual.email == 'KVonnegut@gmail.com'

    def test_Twain(self, setup_authors):
        rs = pytest.sql_runner.select('author', '*', condition = "l_name = 'Twain'")
        actual = pytest.result_formatter.get_first_row(rs)
        assert actual.f_name == 'Mark'
        assert actual.l_name == 'Twain'
        assert actual.email == 'MTwain@gmail.com'

    # this parametrized test does the same thing as both tests above
    @pytest.mark.parametrize('expected', pytest.test_data.authors)
    def test_Authors(self, setup_authors, expected, cur):
        # with pytest.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        with cur as cur:
            sql = 'select * from author where l_name = %s'
            cur.execute(sql, (expected['l_name'],))
            rs = cur.fetchall()
            actual = pytest.result_formatter.get_first_row(rs)
        assert actual.f_name == expected['f_name']
        assert actual.l_name == expected['l_name']
        assert actual.email == expected['email']

