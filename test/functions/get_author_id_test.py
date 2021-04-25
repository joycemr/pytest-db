from pytest import mark
import resources.sql_runner as sql_runner

# test a sql function
@mark.functions
@mark.authors
def test_get_author_id_func(setup_authors):
    test_func = 'get_author_id'
    results = sql_runner.select_one('author', 'id', condition = "l_name = 'Twain'")
    expected_author_id = results[0]
    results = sql_runner.func(test_func, 'Mark Twain')
    author_id = results[0]
    assert expected_author_id == author_id
