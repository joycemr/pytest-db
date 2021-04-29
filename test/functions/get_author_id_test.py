import pytest


test_func = 'get_author_id'

@pytest.fixture
def actual_author_id():
    rs = pytest.sql_runner.select('author', 'id', condition = "l_name = 'Twain'")
    actual = pytest.result_formatter.get_first_row(rs)
    yield actual.id

# test a sql function
@pytest.mark.functions
@pytest.mark.authors
def test_get_author_id_func(setup_authors, actual_author_id):
    results = pytest.sql_runner.function(test_func, 'Mark Twain')
    author_id = results[0]
    assert actual_author_id == author_id
