#!/bin/bash

# db container vars
DB_IMAGE="postgres_sql_test_db"
DB_IMAGE_DOCKERFILE="containers/db/Dockerfile"
DB_MOUNT="type=bind,source="$(pwd)"/containers/db/build,target=/docker-entrypoint-initdb.d"

# pytest image vars
TEST_IMAGE="pytest_sql_test"
TEST_IMAGE_DOCKERFILE="containers/pytest/Dockerfile"
TEST_MOUNT="type=bind,source="$(pwd)"/test,target=/test"

# build the DB_IMAGE if it doesn't exist
OUTPUT=$(docker image ls -q $DB_IMAGE)
if [ ! $OUTPUT ]
    then
    docker build -t $DB_IMAGE -f $DB_IMAGE_DOCKERFILE .
fi

# build the TEST_IMAGE if it doesn't exist
OUTPUT=$(docker image ls -q $TEST_IMAGE)
if [ ! $OUTPUT ]
    then
    docker build -t $TEST_IMAGE -f $TEST_IMAGE_DOCKERFILE .
fi

# start the db container
echo "Starting database"
docker run -d --rm --name ephemeral-test-db --publish 5432:5432 --mount $DB_MOUNT $DB_IMAGE


#TODO do this better
sleep 10

# check for any parameters to the pytest command
if [ $# -eq 0 ]
    then
    docker run --rm --mount $TEST_MOUNT $TEST_IMAGE
else
    docker run --rm --mount $TEST_MOUNT $TEST_IMAGE pytest "$@"
fi

echo "Stopping database"
docker stop ephemeral-test-db
