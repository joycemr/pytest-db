import os
import psycopg2
from psycopg2.extras import NamedTupleCursor

DATABASE_URL = os.getenv("SQL_UNIT_TEST_DB_URL")
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor(cursor_factory=NamedTupleCursor)
