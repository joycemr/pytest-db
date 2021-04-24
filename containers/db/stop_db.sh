#!/bin/bash

docker ps --format '{{.Names}}' | grep sql-unit-test-db

# if running, stop the container
if [ $? -eq 0 ]; then
    docker-compose down --volumes --rmi all &
    wait $!
else
    echo The sql-unit-test-db container is not running
    exit 0
fi

# check if stopped
docker ps --format '{{.Names}}' | grep sql-unit-test-db
if [ $? -eq 0 ]; then
    echo The sql-unit-test-db container failed to stop
else
    echo The sql-unit-test-db container is stopped
fi
