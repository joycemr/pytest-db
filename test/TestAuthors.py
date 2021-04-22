from pytest import mark
import sql_runner

@mark.authors
class TestAuthors:

    # using the custom sql_runner
    def test_Vonnegut(self, setup_authors):
        result = sql_runner.select_all('author', "l_name = 'Vonnegut'")
        print(result)
        assert 'Kurt' == result[0][1]
        assert 'Vonnegut' == result[0][2]
        assert 'KVonnegut@gmail.com' == result[0][3]

    # using the psycopg2 connection directly
    def test_Twain(self, setup_authors, cur):
        sql = "select * from author where l_name = 'Twain';"
        cur.execute(sql)
        result = cur.fetchone()
        assert 'Mark' == result[1]
        assert 'Twain' == result[2]
        assert 'MTwain@gmail.com' == result[3]

    # test a sql function
    def test_get_author_id_func(self, setup_authors):
        test_func = 'get_author_id'
        results = sql_runner.select_one('author', 'id', condition = "l_name = 'Twain'")
        expected_author_id = results[0]
        results = sql_runner.func(test_func, 'Mark Twain')
        author_id = results[0]
        assert expected_author_id == author_id
