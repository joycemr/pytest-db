from resources.convert_var import convert_var
from resources.db import conn
from psycopg2.extras import NamedTupleCursor


def select(table_name, *field_list, condition = 'true'):
    sql = "SELECT " + ", ".join(["{}"]*len(field_list)).format(*field_list)+" FROM {} WHERE {}".format(table_name, condition)
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql)
        return cur.fetchall()

def insert(table_name, *args):
    var_list = [convert_var(var) for var in args]
    sql = "INSERT INTO "+table_name+" VALUES (" + ", ".join(["{}"]*len(var_list)).format(*var_list) + ");"
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql)
        return cur.fetchone()

def delete(table_name, condition = 'true'):
    sql = "DELETE FROM {} WHERE {}".format(table_name, condition)
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql)
        return cur.fetchone()

def function(function_name, *args):
    var_list = [convert_var(var) for var in args]
    sql = "SELECT " + function_name + "(" + ", ".join(["{}"]*len(var_list)).format(*var_list) + ");"
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql)
        return cur.fetchone()

def function_row_type(function_name, dict):
    var_list = [convert_var(value) for key, value in dict.items()]
    sql = "SELECT " + function_name + "((" + ", ".join(["{}"]*len(var_list)).format(*var_list) + "));"
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql)
        return cur.fetchone()
