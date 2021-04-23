
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