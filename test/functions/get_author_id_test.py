import pytest


test_func = 'get_author_id'

@pytest.fixture
def expected():
    rs = pytest.sql_runner.select('author', 'id', condition = "l_name = 'Twain'")
    actual = pytest.sql_formatter.get_first_row(rs)
    return actual

# test a sql function
@pytest.mark.functions
@pytest.mark.authors
def test_get_author_id_func(setup_authors, expected, no_data_msg):
    results = pytest.sql_runner.function(test_func, 'Mark Twain')
    try:
        actual_author_id = pytest.sql_formatter.get_first_row(results).get_author_id
        assert expected.id == actual_author_id
    except:
        assert False, no_data_msg
