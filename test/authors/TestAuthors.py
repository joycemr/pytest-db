from pytest import mark
from db import cur
import sql_runner

@mark.authors
class TestAuthors:

    # using the custom sql_runner
    @mark.Vonnegut
    def test_Vonnegut(self, setup_authors):
        result = sql_runner.select_all('author', "l_name = 'Vonnegut'")
        print(result)
        assert 'Kurt' == result[0].f_name
        assert 'Vonnegut' == result[0].l_name
        assert 'KVonnegut@gmail.com' == result[0].email

    # using the psycopg2 connection directly
    @mark.Twain
    def test_Twain(self, setup_authors):
        sql = "select * from author where l_name = 'Twain';"
        cur.execute(sql)
        result = cur.fetchone()
        assert 'Mark' == result.f_name
        assert 'Twain' == result.l_name
        assert 'MTwain@gmail.com' == result.email

    # test a sql function
    def test_get_author_id_func(self, setup_authors):
        test_func = 'get_author_id'
        results = sql_runner.select_one('author', 'id', condition = "l_name = 'Twain'")
        expected_author_id = results[0]
        results = sql_runner.func(test_func, 'Mark Twain')
        author_id = results[0]
        assert expected_author_id == author_id
