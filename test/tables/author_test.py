from pytest import mark
from resources.db import cur
import resources.sql_runner as sql_runner

@mark.authors
@mark.tables
class TestAuthors:

    # using the custom sql_runner
    def test_Vonnegut(self, setup_authors):
        result = sql_runner.select_all('author', "l_name = 'Vonnegut'")
        print(result)
        assert 'Kurt' == result[0].f_name
        assert 'Vonnegut' == result[0].l_name
        assert 'KVonnegut@gmail.com' == result[0].email

    # using the psycopg2 connection directly
    def test_Twain(self, setup_authors):
        sql = "select * from author where l_name = 'Twain';"
        cur.execute(sql)
        result = cur.fetchone()
        assert 'Mark' == result.f_name
        assert 'Twain' == result.l_name
        assert 'MTwain@gmail.com' == result.email
