#!/bin/bash

# db container vars
DB_IMAGE="postgres_sql_test_db"
DB_CONTAINER="ephemeral-test-db"
DB_IMAGE_DOCKERFILE="containers/db/Dockerfile"

# pytest image vars
TEST_IMAGE="pytest_sql_test"
TEST_IMAGE_DOCKERFILE="containers/pytest/Dockerfile"
TEST_MOUNT="type=bind,source="$(pwd)"/test,target=/test"

# functions
rebuild_db_container () {
    OUTPUT=$(docker image ls -q $DB_IMAGE)
    if [ $OUTPUT ]
        then
        docker image rm $DB_IMAGE
    fi
    docker build -t $DB_IMAGE -f $DB_IMAGE_DOCKERFILE .
}

rebuild_test_container () {
    OUTPUT=$(docker image ls -q $TEST_IMAGE)
    if [ $OUTPUT ]
        then
        docker image rm $TEST_IMAGE
    fi
    docker build -t $TEST_IMAGE -f $TEST_IMAGE_DOCKERFILE .
}

wait_on_db_connection () {
    until docker exec $DB_CONTAINER pg_isready ; do sleep 3 ; done
}

if [ "$1" == "rebuild" ]
    then # rebuild the images
    shift # throw away 1st parameter any others will be passed to pytest
    echo "Rebuilding the container images..."
    rebuild_db_container
    rebuild_test_container
else
    # build the DB_IMAGE if it doesn't exist
    OUTPUT=$(docker image ls -q $DB_IMAGE)
    if [ ! $OUTPUT ]
        then
        rebuild_db_container
    fi

    # build the TEST_IMAGE if it doesn't exist
    OUTPUT=$(docker image ls -q $TEST_IMAGE)
    if [ ! $OUTPUT ]
        then
        rebuild_test_container
    fi
fi

# start the db container
echo "Starting database"
docker run -d --rm --name $DB_CONTAINER --publish 5432:5432 $DB_IMAGE

# wait until the DB_CONTAINER is accepting connections
wait_on_db_connection

# check for any parameters to the pytest command
if [ $# -eq 0 ]
    then
    docker run --rm --mount $TEST_MOUNT $TEST_IMAGE
else
    docker run --rm --mount $TEST_MOUNT $TEST_IMAGE pytest "$@"
fi

echo "Stopping database"
docker stop ephemeral-test-db
