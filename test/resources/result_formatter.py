
def get_first_row(rs):
    if type(rs) != list:
        return rs
    else:
        if len(rs) > 0:
            return rs[0]
