from pytest import mark
import sql_runner

def test_Vonnegut(setup_authors, cur):
    sql = "select * from author where l_name = 'Vonnegut';"
    cur.execute(sql)
    result = cur.fetchone()
    assert True
    assert 'Kurt' == result[1]
    assert 'Vonnegut' == result[2]
    assert 'KVonnegut@gmail.com' == result[3]

def test_Twain(setup_authors, cur):
    sql = "select * from author where l_name = 'Twain';"
    cur.execute(sql)
    result = cur.fetchone()
    assert 'Mark' == result[1]
    assert 'Twain' == result[2]
    assert 'MTwain@gmail.com' == result[3]

# def test_get_author_id_func(setup_authors, cur):
#     test_func = 'get_author_id'
#     # get the expected author_id
#     expected_author_id = sql_runner.select_one('author', cur, 'id', "l_name = 'Twain")
#     # sql = "select id from author where l_name = 'Twain';"
#     # cur.execute(sql)
#     # expected_author_id = cur.fetchone()
#     print(expected_author_id)

#     author_db = sql_runner.func(test_func, cur, 'Mark Twain')
#     print(author_db)
#     assert expected_author_id == author_db
