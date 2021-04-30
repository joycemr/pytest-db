import pytest
from resources.convert_var import convert_var
import resources.sql_formatter as sql_formatter
from psycopg2.extras import NamedTupleCursor
import sys


def run_sql(sql, params=False):
    with pytest.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        try:
            if params:
                cur.execute(sql, params)
            else:
                cur.execute(sql)
            return cur.fetchall()
        except:
            pytest.conn.rollback()


def select(table_name, *field_list, condition = 'true'):
    sql = "SELECT " + ", ".join(["{}"]*len(field_list)).format(*field_list)+" FROM {} WHERE {}".format(table_name, condition)
    return run_sql(sql)

def insert(table_name, data_dict):
    sql = sql_formatter.insert(table_name, data_dict)
    return run_sql(sql, data_dict)

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
