from convert_var import convert_var
from db import cur

def func(function_name, *args):
    var_list = [convert_var(var) for var in args]
    sql = "SELECT " + function_name + "(" + ", ".join(["{}"]*len(var_list)).format(*var_list) + ");"
    print(sql)
    cur.execute(sql)
    return cur.fetchone()

def select_one(table_name, *field_list, condition = 'true'):
    sql = "SELECT " + ", ".join(["{}"]*len(field_list)).format(*field_list)+" FROM {} WHERE {}".format(table_name, condition)
    print(sql)
    cur.execute(sql)
    return cur.fetchone()

def select_all(table_name, condition = 'true'):
    sql = "SELECT * FROM {} WHERE {}".format(table_name, condition)
    print(sql)
    cur.execute(sql)
    return cur.fetchall()

def func_row_type(function_name, dict):
    var_list = [convert_var(value) for key, value in dict.items()]
    sql = "SELECT " + function_name + "((" + ", ".join(["{}"]*len(var_list)).format(*var_list) + "));"
    print(sql)
    cur.execute(sql)
    return cur.fetchone()

def insert(table_name, *args):
    var_list = [convert_var(var) for var in args]
    sql = "INSERT INTO "+table_name+" VALUES (" + ", ".join(["{}"]*len(var_list)).format(*var_list) + ");"
    print(sql)
    cur.execute(sql)
    return cur.fetchone()

def delete(table_name, condition = 'true'):
    sql = "DELETE FROM {} WHERE {}".format(table_name, condition)
    cur.execute(sql)
    return cur.fetchone()
