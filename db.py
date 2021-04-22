import os
import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.getenv("SQL_UNIT_TEST_DB_URL")
conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
