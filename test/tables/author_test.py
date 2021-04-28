from pytest import mark
from resources.sql_runner import select
from resources.result_formatter import get_first_row

@mark.authors
@mark.tables
class TestAuthors:

    def test_Vonnegut(self, setup_authors):
        rs = select('author', '*', condition = "l_name = 'Vonnegut'")
        actual = get_first_row(rs)
        assert actual.f_name == 'Kurt'
        assert actual.l_name == 'Vonnegut'
        assert actual.email == 'KVonnegut@gmail.com'

    def test_Twain(self, setup_authors):
        rs = select('author', '*', condition = "l_name = 'Twain'")
        actual = get_first_row(rs)
        print(actual)
        assert actual.f_name == 'Mark'
        assert actual.l_name == 'Twain'
        assert actual.email == 'MTwain@gmail.com'
