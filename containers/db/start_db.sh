#!/bin/bash

docker ps --format '{{.Names}}' | grep sql-unit-test-db

# if running stop container
if [ $? -eq 0 ]; then
    ./stop_db.sh
    sleep 10
fi

# start container
docker-compose up -d --build
sleep 5

# quick health check
docker stats sql-unit-test-db --no-stream

if [ $? -eq 0 ]; then
    echo The sql-unit-test-db container is up
else
    echo There was a problem with starting the sql-unit-test-db container
fi
