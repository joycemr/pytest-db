#!/bin/bash

# pytest image vars
TEST_IMAGE="pytest_sql_test"
TEST_IMAGE_DOCKERFILE="containers/pytest/Dockerfile"
TEST_MOUNT="type=bind,source="$(pwd)"/test,target=/test"

# build the TEST_IMAGE if it doesn't exist
OUTPUT=$(docker image ls -q $TEST_IMAGE)
if [ ! $OUTPUT ]
    then
    docker build -t $TEST_IMAGE -f $TEST_IMAGE_DOCKERFILE .
fi

# check for any parameters to the pytest command
if [ $# -eq 0 ]
    then
    docker run --rm --mount $TEST_MOUNT  $TEST_IMAGE
else
    docker run --rm --mount $TEST_MOUNT  $TEST_IMAGE pytest "$@"
fi
