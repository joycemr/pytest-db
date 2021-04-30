import pytest
from resources.convert_var import convert_var
from resources.sql_formatter import get_field_list, get_param_placeholders
from psycopg2.extras import NamedTupleCursor
import sys


def run_sql(sql):
    with pytest.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        try:
            cur.execute(sql)
            return cur.fetchall()
        except:
            pytest.conn.rollback()

def run_sql_with_params(sql, params):
    with pytest.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        try:
            cur.execute(sql, params)
            return cur.fetchall()
        except:
            pytest.conn.rollback()


def select(table_name, *field_list, condition = 'true'):
    sql = "SELECT " + ", ".join(["{}"]*len(field_list)).format(*field_list)+" FROM {} WHERE {}".format(table_name, condition)
    return run_sql(sql)

def insert(table_name, data_dict):
    sql = "INSERT INTO " + table_name + "(" + get_field_list(data_dict) + ") VALUES (" + get_param_placeholders(data_dict) + ") RETURNING *"
    return run_sql_with_params(sql, data_dict)

def delete(table_name, condition = 'true'):
    sql = "DELETE FROM {} WHERE {}".format(table_name, condition)
    return run_sql(sql)

def function(function_name, *args):
    var_list = [convert_var(var) for var in args]
    sql = "SELECT " + function_name + "(" + ", ".join(["{}"]*len(var_list)).format(*var_list) + ")"
    return run_sql(sql)

def function_row_type(function_name, dict):
    var_list = [convert_var(value) for key, value in dict.items()]
    sql = "SELECT " + function_name + "((" + ", ".join(["{}"]*len(var_list)).format(*var_list) + "))"
    return run_sql(sql)
