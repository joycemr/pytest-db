def get_field_list(data_dict):
    return ', '.join(['{}']*len(data_dict)).format(*data_dict.keys())

def get_param_placeholders(data_dict):
    return ', '.join(['%({})s']*len(data_dict)).format(*data_dict)

def select(table_name, *field_list, condition = 'true'):
    sql = ["SELECT "]
    sql.append(", ".join(["{}"]*len(field_list)).format(*field_list))
    sql.append(" FROM {} ".format(table_name))
    sql.append(" WHERE {}".format(condition))
    return ''.join(sql)

def insert(table_name, data_dict):
    sql = ['INSERT INTO ' + table_name]
    sql.append('(' + get_field_list(data_dict) + ')')
    sql.append(' VALUES (' + get_param_placeholders(data_dict) + ')')
    sql.append(' RETURNING *')
    return ''.join(sql)

def convert_var(var):
    if var is None:
        function_variable = 'null'
    elif isinstance(var,str):
        function_variable = "'{}'".format(var)
    elif isinstance(var,int):
        function_variable = "{}".format(var)
    else:
        function_variable = var

    return function_variable
