import pytest
import resources.sql_formatter as sql_formatter

@pytest.mark.resources
def test_insert(table, data_dict, expected_insert_sql):
    assert expected_insert_sql == sql_formatter.insert(table, data_dict)
