import pytest


@pytest.mark.authors
@pytest.mark.tables
class TestAuthors:

    def test_Vonnegut(self, setup_authors, no_data_msg):
        rs = pytest.sql_runner.select('author', '*', condition = "l_name = 'Vonnegut'")
        try:
            actual = pytest.sql_runner.get_first_row(rs)
            assert actual.f_name == 'Kurt'
            assert actual.l_name == 'Vonnegut'
            assert actual.email == 'KVonnegut@gmail.com'
        except:
            assert False, no_data_msg

    def test_Twain(self, setup_authors):
        rs = pytest.sql_runner.select('author', '*', condition = "l_name = 'Twain'")
        try:
            actual = pytest.sql_runner.get_first_row(rs)
            assert actual.f_name == 'Mark'
            assert actual.l_name == 'Twain'
            assert actual.email == 'MTwain@gmail.com'
        except:
            assert False, no_data_msg

    # this parametrized test does the same thing as both tests above
    @pytest.mark.parametrize('expected', pytest.test_data.authors)
    def test_Authors(self, setup_authors, expected):
        where_clause = "l_name = '" + expected['l_name'] + "'"
        rs = pytest.sql_runner.select('author', '*', condition = where_clause)
        try:
            actual = pytest.sql_runner.get_first_row(rs)
            assert actual.f_name == expected['f_name']
            assert actual.l_name == expected['l_name']
            assert actual.email == expected['email']
        except:
            assert False, no_data_msg

    # example of a test that is not ready for some reason
    @pytest.mark.skip(reason='Code not ready yet')
    def test_that_is_not_ready(self):
        assert False

    # example of a test with an expected failure
    @pytest.mark.xfail(reason='deprecated feature')
    def test_expected_to_fail(self):
        assert False