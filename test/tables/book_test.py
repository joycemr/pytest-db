import pytest


@pytest.mark.books
@pytest.mark.tables
class TestBooks:

    @pytest.mark.parametrize('expected', pytest.test_data.books)
    def test_books(self, setup_authors, setup_books, no_data_msg, expected):
        # TODO I have to deal with the strings that have single quotes here
        # this is kludgy
        title_condition = "title = '" + expected['title'].replace("'","''") + "'"
        print(title_condition)
        rs = pytest.sql_runner.select('book', '*', condition = title_condition)
        try:
            actual = pytest.sql_runner.get_first_row(rs)
            assert actual.title == expected['title']
            assert actual.pub_year == expected['pub_year']
        except:
            assert False, no_data_msg