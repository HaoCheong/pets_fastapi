#!/bin/bash

run_option=$1
local_path="/home/hcheong/Desktop/Other/pets_fastapi"

if [[ $run_option == "demo" ]]; then
    set -a && source demo.env && set +a
    docker compose --env-file $local_path/demo.env -f docker-compose.yml up --force-recreate --remove-orphans -d
    echo "==================== ACCESS POINTS (${PROJECT_NAME}) ===================="
    echo "BACKEND URL -> $BACKEND_CONTAINER_URL"
    echo "DB Access -> PGPASSWORD=${PETS_POSTGRES_DB_PASS} PAGER='less -S' psql -h ${PETS_POSTGRES_DB_HOST} -p ${PETS_POSTGRES_DB_PORT} -d ${PETS_POSTGRES_DB_NAME} -U ${PETS_POSTGRES_DB_USER}"
    echo "================================== END =================================="
    exit 0
fi

if [[ $run_option == "live" ]]; then
    set -a && source live.env && set +a
    docker compose --env-file $local_path/live.env -f docker-compose.yml up --force-recreate --remove-orphans -d 
    echo "==================== ACCESS POINTS (${PROJECT_NAME}) ===================="
    echo "BACKEND URL -> $BACKEND_CONTAINER_URL"
    echo "DB Access -> PGPASSWORD=${PETS_POSTGRES_DB_PASS} PAGER='less -S' psql -h ${PETS_POSTGRES_DB_HOST} -p ${PETS_POSTGRES_DB_PORT} -d ${PETS_POSTGRES_DB_NAME} -U ${PETS_POSTGRES_DB_USER}"
    echo "================================== END =================================="
    exit 0
fi

if [[ $run_option == "unit" ]]; then
    set -a && source demo.env && set +a
    docker compose --env-file $local_path/demo.env -f docker-compose-test.yml up --force-recreate --remove-orphans -d
    sleep 1
    python3 -m pytest -v tests/unit/owner_tests.py
    python3 -m pytest -v tests/unit/nutrition_plan_tests.py
    python3 -m pytest -v tests/unit/trainer_tests.py
    python3 -m pytest -v tests/unit/pet_tests.py
    python3 -m pytest -v tests/unit/pet_assignment_tests.py
fi


if [[ $run_option == "stop" ]]; then
    docker compose --env-file $local_path/demo.env stop 
    docker compose --env-file $local_path/demo.env down -v

    docker compose --env-file $local_path/live.env stop 
    docker compose --env-file $local_path/live.env down -v
    exit 0
fi

echo "USAGE: ./run.sh [demo|live|unit|stop]"