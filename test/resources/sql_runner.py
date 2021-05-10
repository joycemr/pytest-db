import pytest
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
    sql = sql_formatter.select(table_name, *field_list, condition = condition)
    return run_sql(sql)

def insert(table_name, data_dict):
    sql = sql_formatter.insert(table_name, data_dict)
    return run_sql(sql, data_dict)

def delete(table_name, condition = 'true'):
    sql = sql_formatter.delete(table_name, condition = condition)
    return run_sql(sql)

def function(function_name, *args, row_type = False):
    sql = sql_formatter.function(function_name, *args, row_type = row_type)
    return run_sql(sql)

def get_first_row(rs):
    if type(rs) != list:
        return rs
    else:
        if len(rs) > 0:
            return rs[0]

def print_select(sql):
    with pytest.conn.cursor() as cur:
        cur.execute(sql)
        rs = cur.fetchall()
        for row in rs:
            print(row)
