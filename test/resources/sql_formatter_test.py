import pytest
import resources.sql_formatter as sql_formatter
import resources.sql_runner as sql_runner

@pytest.fixture(scope='function')
def table():
    yield  'author'

@pytest.fixture(scope='function')
def data_dict():
    return {'id': 1, 'f_name': 'Kurt', 'l_name': 'Vonnegut', 'email': 'KVonnegut@gmail.com'}

@pytest.fixture(scope='function')
def expected_field_list():
    return 'id, f_name, l_name, email'

@pytest.fixture(scope='function')
def expected_param_placeholders():
    return '%(id)s, %(f_name)s, %(l_name)s, %(email)s'

@pytest.fixture(scope='function')
def expected_insert_sql():
    return 'INSERT INTO author(id, f_name, l_name, email) VALUES (%(id)s, %(f_name)s, %(l_name)s, %(email)s) RETURNING *'

@pytest.fixture
def expected_function_call():
    return "SELECT get_author_id(1, 'Mark Twain')"

@pytest.mark.resources
class TestSqlFormatter:

    def test_get_field_list(self, data_dict, expected_field_list):
        assert expected_field_list == sql_formatter.get_field_list(data_dict)

    def test_get_param_placeholders(self, data_dict, expected_param_placeholders):
        assert expected_param_placeholders == sql_formatter.get_param_placeholders(data_dict)

    def test_insert(self, table, data_dict, expected_insert_sql):
        assert expected_insert_sql == sql_formatter.insert(table, data_dict)

    def test_func(self, expected_function_call):
        assert expected_function_call == sql_formatter.function('get_author_id', 1, 'Mark Twain')

