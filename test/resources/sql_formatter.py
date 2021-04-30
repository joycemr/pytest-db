
def get_first_row(rs):
    if type(rs) != list:
        return rs
    else:
        if len(rs) > 0:
            return rs[0]

def get_field_list(data_dict):
    return ", ".join(["{}"]*len(data_dict)).format(*data_dict.keys())

def get_param_placeholders(data_dict):
    return ", ".join(["%({})s"]*len(data_dict)).format(*data_dict)
