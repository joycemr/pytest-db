from pytest import fixture, mark
from resources.sql_runner import select, function
from resources.result_formatter import get_first_row

test_func = 'get_author_id'

@fixture
def actual_author_id():
    rs = select('author', 'id', condition = "l_name = 'Twain'")
    actual = get_first_row(rs)
    yield actual.id

# test a sql function
@mark.functions
@mark.authors
def test_get_author_id_func(setup_authors, actual_author_id):
    results = function(test_func, 'Mark Twain')
    author_id = results[0]
    assert actual_author_id == author_id
