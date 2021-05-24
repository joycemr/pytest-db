# sql-unit-test-template

## Purpose

## Structure

## Test Data

- All test data is in .csv form. This was used because it allows the pytest suite to use the same data that can be loaded directly into the database with the postgreSQL copy utility.

- test/data/author.csv
  - Two test rows for the author table.
- test/data/book.csv
  - Eight test rows for the book table.

- To load the data directly with psql
  - start the database container manually
  - in psql, from the parent directory run
    ```
    \copy author from test/data/author.csv with CSV HEADER;
    \copy book from test/data/book.csv with CSV HEADER;
    ```
