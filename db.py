import os
import psycopg2

DATABASE_URL = os.getenv("SQL_UNIT_TEST_DB_URL")
conn = psycopg2.connect(DATABASE_URL)
print(conn)
