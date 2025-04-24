#!/bin/bash

# New Running System: Encompasses testing, live deving and production setup all under one roof

# Usage: ./run.sh <RUN_OPTION> 

# vvvvvvvvvvvvvvvvvvvv CONFIGURATION vvvvvvvvvvvvvvvvvvvv

PROJECT_NAME="Pets FastAPI 'Prod''"
LOCAL_PROJECT_PATH=/home/hcheong/Desktop/Other/pets_fastapi

PETS_POSTGRES_DB_USER="prod_pets_user"
PETS_POSTGRES_DB_PASS="prod_pets_pass"
PETS_POSTGRES_DB_NAME="prod_pets_database"
PETS_POSTGRES_DB_HOST="10.1.50.133"
PETS_POSTGRES_DB_PORT="8501"
PETS_SQL_DUMP_FILE_PATH="${LOCAL_PROJECT_PATH}/utils/test_pets_dump.sql"
PETS_SQL_DUMP_SCHEMA_ONLY=0
PETS_CONTAINER_NAME="pets_prod_database_cont"
PETS_IMAGE_NAME="postgres:14.5"
PETS_TIMEZONE="Australia/Sydney"

BACKEND_PORT=8502
BACKEND_APP_PATH="${LOCAL_PROJECT_PATH}"
BACKEND_CONTAINER_URL="http://${PETS_POSTGRES_DB_HOST}:${BACKEND_PORT}"
BACKEND_CONTAINER_NAME="pets_fastapi_prod_backend_cont"
BACKEND_IMAGE_NAME="pets_fastapi_backend_img"
BACKEND_TIMEZONE="Australia/Sydney"

BACKEND_ENV="${LOCAL_PROJECT_PATH}/.venv"

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

source "${LOCAL_PROJECT_PATH}/utils/container_utils.sh"
source "${LOCAL_PROJECT_PATH}/utils/pg_container_utils.sh"

function show_container_status {
    # Displays the container status

    echo "========== CONTAINERS STATUS =========="
    docker ps
}

function show_container_url {
    # Displays the access container for required access

    container_url=$1
    container_name=$2

    echo "========== ACCESS URL for CONTAINER: ${container_name} =========="
    echo "> ${container_url}"
}

function run_backend {
    # Runs the backend container (CHANGE REQUIRED PER PROJECT)

    docker run -p ${BACKEND_PORT}:8000 \
        -d \
        -e "PETS_POSTGRES_DB_USER=${PETS_POSTGRES_DB_USER}" \
        -e "PETS_POSTGRES_DB_PASS=${PETS_POSTGRES_DB_PASS}" \
        -e "PETS_POSTGRES_DB_NAME=${PETS_POSTGRES_DB_NAME}" \
        -e "PETS_POSTGRES_DB_HOST=${PETS_POSTGRES_DB_HOST}" \
        -e "PETS_POSTGRES_DB_PORT=${PETS_POSTGRES_DB_PORT}" \
        -e "TZ=${BACKEND_TIMEZONE}" \
        --mount type=bind,source="${BACKEND_APP_PATH}/app",target=/app/ \
        --name ${BACKEND_CONTAINER_NAME} ${BACKEND_IMAGE_NAME}
}


run_option=$1

if [[ $run_option == "start" ]]; then
    # Running a live demo with sample data
    echo "========== RUNNING PRODUCTION MODE ($PROJECT_NAME) =========="

    # Pull Image
    pull_image $PETS_IMAGE_NAME

    # Tear down any existing DB container (ignore image)
    remove_containers $PETS_CONTAINER_NAME

    # Spin up DB container (Pull image if it does not exist)
    run_pg_container $PETS_POSTGRES_DB_USER $PETS_POSTGRES_DB_PASS $PETS_POSTGRES_DB_NAME $PETS_POSTGRES_DB_HOST $PETS_POSTGRES_DB_PORT $PETS_CONTAINER_NAME $PETS_IMAGE_NAME $PETS_TIMEZONE
    load_pg_dump_file $PETS_POSTGRES_DB_USER $PETS_POSTGRES_DB_PASS $PETS_POSTGRES_DB_NAME $PETS_POSTGRES_DB_HOST $PETS_POSTGRES_DB_PORT $PETS_SQL_DUMP_FILE_PATH
    clear_content_pg_file $PETS_POSTGRES_DB_USER $PETS_POSTGRES_DB_PASS $PETS_POSTGRES_DB_NAME $PETS_POSTGRES_DB_HOST $PETS_POSTGRES_DB_PORT $PETS_SQL_DUMP_SCHEMA_ONLY

    # Tear down Application Containers
    remove_containers $BACKEND_CONTAINER_NAME

    # Build Application Containers
    build_image $BACKEND_IMAGE_NAME $BACKEND_APP_PATH

    # Spin up Frontend Container
    run_backend

    sleep 1

    # Show the container statuses
    show_container_status

    # Show Container Links
    show_container_url $BACKEND_CONTAINER_URL $BACKEND_CONTAINER_NAME

    # Show DB Access
    show_pg_access_cmd $PETS_POSTGRES_DB_USER $PETS_POSTGRES_DB_PASS $PETS_POSTGRES_DB_NAME $PETS_POSTGRES_DB_HOST $PETS_POSTGRES_DB_PORT $PETS_CONTAINER_NAME
fi

if [[ $run_option == "stop" ]]; then

    # Stop and remove all containers
    remove_containers $PETS_CONTAINER_NAME
    remove_containers $BACKEND_CONTAINER_NAME

    exit 1
fi

if [[ $run_option == "build" ]]; then 
    # Stop and remove all containers (CHANGE REQUIRED PER PROJECT)
    
    build_image $BACKEND_IMAGE_NAME $BACKEND_APP_PATH
fi

if [[ $run_option == "clean" ]]; then 
    # Stop and remove all containers and image
    remove_containers $PETS_CONTAINER_NAME

    remove_containers $BACKEND_CONTAINER_NAME
    
    remove_image $PETS_IMAGE_NAME

    remove_image $BACKEND_IMAGE_NAME
fi

if [[ $run_option == "help" ]]; then
    # Show Usage
    echo "========== USAGE =========="
    echo "> ./run.sh build - Build and required containers"
    echo "> ./run.sh start - Builds the environment and runs demo/dev. Resets any databases"
    echo "> ./run.sh stop - Stops and remove all running containers. Resets any databases"
    echo "> ./run.sh clean - Stop and remove all containers AND images. Clears any databases"
    echo "> ./run.sh help - Shows all the possible options"
fi