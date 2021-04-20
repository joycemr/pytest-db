from pytest import mark

def test_Vonnegut(setup_authors_dispose, cur):
    sql = "select * from author where l_name = 'Vonnegut';"
    cur.execute(sql)
    result = cur.fetchone()
    assert True
    assert 'Kurt' == result[1]
    assert 'Vonnegut' == result[2]
    assert 'KVonnegut@gmail.com' == result[3]

def test_Twain(setup_authors_dispose, cur):
    sql = "select * from author where l_name = 'Twain';"
    cur.execute(sql)
    result = cur.fetchone()
    assert 'Mark' == result[1]
    assert 'Twain' == result[2]
    assert 'MTwain@gmail.com' == result[3]
