import os, sys
import psycopg2

class NoDatabaseUrlSet(Exception):
    pass

# for testing
# local
# export SQL_UNIT_TEST_TEMPLATE_DB_URL=postgresql://postgres:postgres@localhost:5432/postgres
# container
# export SQL_UNIT_TEST_TEMPLATE_DB_URL=postgresql://postgres:postgres@host.docker.internal:5432/postgres
DATABASE_URL = os.getenv("SQL_UNIT_TEST_TEMPLATE_DB_URL")
if DATABASE_URL == None:
    raise NoDatabaseUrlSet('The environment variable SQL_UNIT_TEST_TEMPLATE_DB_URL needs to be set to point the the test database')
    sys.exit(0)

conn = psycopg2.connect(DATABASE_URL)
