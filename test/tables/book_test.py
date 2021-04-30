import pytest


@pytest.mark.books
@pytest.mark.tables
class TestBooks:

    def test_Vonnegut(self, setup_authors, setup_books, no_data_msg):
        rs = pytest.sql_runner.select('book', '*', condition = "title = 'Slaughterhouse-Five'")
        try:
            actual = pytest.sql_runner.get_first_row(rs)
            assert actual.title == 'Slaughterhouse-Five'
            assert actual.pub_year == '1969'
        except:
            assert False, no_data_msg