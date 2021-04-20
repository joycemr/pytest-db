import psycopg2
conn = psycopg2.connect('postgresql://postgres:postgres@localhost:5435/midb')

def get_table_dict(table_name):
    dict = {}
    cur = conn.cursor()
    cur.execute("select column_name from information_schema.columns where table_schema = 'midb' and table_name = %s;", (table_name,))
    rs = cur.fetchall()
    for row in rs:
        dict[row[0]] = None
    return dict

def get_object_dict():
    dict = {}
    cur = conn.cursor()
    cur.execute("select table_name from information_schema.tables where table_schema = 'midb';")
    rs = cur.fetchall()
    for row in rs:
        dict[row[0]] = get_table_dict(row[0])
    return dict

object_dict = get_object_dict()
print(object_dict['eqp'])
