#!/bin/bash

# build the pytest_sql_test image if it doesn't exist
OUTPUT=$(docker image ls -q pytest_sql_test)
if [ ! $OUTPUT ]
    then
    docker build -t pytest_sql_test -f containers/pytest/Dockerfile .
fi

# check for any parameters to the pytest_sql_test command
if [ $# -eq 0 ]
    then
    docker run --name pytest_sql_test --mount type=bind,source="$(pwd)"/test,target=/test --rm  pytest_sql_test
else
    docker run --name pytest_sql_test --mount type=bind,source="$(pwd)"/test,target=/test --rm  pytest_sql_test pytest "$@"
fi
