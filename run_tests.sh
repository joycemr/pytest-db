#!/bin/bash

# db script vars
DB_BUILD_DIR="db/build"
DB_TABLE_DIR="db/tables"
DB_FUNCTION_DIR="db/functions"

# db container vars
DB_IMAGE="postgres_sql_test_db"
DB_CONTAINER="ephemeral-test-db"
DB_IMAGE_DOCKERFILE="containers/db/Dockerfile"

# pytest image vars
TEST_IMAGE="pytest_sql_test"
TEST_IMAGE_DOCKERFILE="containers/pytest/Dockerfile"
TEST_MOUNT="type=bind,source="$(pwd)"/test,target=/test"

# functions
build_database_sql () {
    cat $DB_TABLE_DIR/*.sql > $DB_BUILD_DIR/complete.sql
    cat $DB_FUNCTION_DIR/*.sql >> $DB_BUILD_DIR/complete.sql
}

rebuild_db_image () {
    OUTPUT=$(docker image ls -q $DB_IMAGE)
    if [ $OUTPUT ]
        then
        docker image rm $DB_IMAGE
    fi
    docker build -t $DB_IMAGE -f $DB_IMAGE_DOCKERFILE .
}

rebuild_test_image () {
    OUTPUT=$(docker image ls -q $TEST_IMAGE)
    if [ $OUTPUT ]
        then
        docker image rm $TEST_IMAGE
    fi
    docker build -t $TEST_IMAGE -f $TEST_IMAGE_DOCKERFILE .
}

check_db_connection () {
    docker exec $DB_CONTAINER pg_isready
}

wait_on_db_connection () {
    for i in {1..10}; do
        check_db_connection
        if [ $? -eq 0 ]
            then return
        fi
        sleep 2
    done
    echo 'cannot connect to db container'
    exit
}

# rebuild the database SQL DDL file
build_database_sql

# check if the first parameter = "rebuild"
# if so, rebuild all the containers
# else, check for the images and build them as necessary
if [ "$1" == "rebuild" ]
    then
    shift # throw away 1st parameter any others will be passed to pytest
    echo "Rebuilding the container images..."
    rebuild_db_image
    rebuild_test_image
else
    OUTPUT=$(docker image ls -q $DB_IMAGE)
    if [ ! $OUTPUT ]
        then
        rebuild_db_image
    fi
    OUTPUT=$(docker image ls -q $TEST_IMAGE)
    if [ ! $OUTPUT ]
        then
        rebuild_test_image
    fi
fi

# start the db container
echo "Starting database"
docker run -d --rm --name $DB_CONTAINER --publish 5432:5432 $DB_IMAGE

# wait until the DB_CONTAINER is accepting connections
wait_on_db_connection

# start the pytest container
# we don't name it or need to stop it, it only runs the command and then stops
# if no parameters, just run the container
# if parameters, override the image command with a new one containing the parameters
if [ $# -eq 0 ]
    then
    docker run --rm --mount $TEST_MOUNT $TEST_IMAGE
else
    docker run --rm --mount $TEST_MOUNT $TEST_IMAGE pytest "$@"
fi

# stop the db container
echo "Stopping database"
docker stop ephemeral-test-db
