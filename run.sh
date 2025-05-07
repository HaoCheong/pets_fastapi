run_option=$1
local_path="/home/hcheong/Desktop/Other/pets_fastapi"

if [[ $run_option == "demo" ]]; then
    source demo.env
    docker compose --env-file $local_path/demo.env up --force-recreate --remove-orphans -d
    echo "==================== ACCESS POINTS (${PROJECT_NAME}) ===================="
    echo "BACKEND URL -> $BACKEND_CONTAINER_URL"
    echo "DB Access -> PGPASSWORD=${PETS_POSTGRES_DB_PASS} PAGER='less -S' psql -h ${PETS_POSTGRES_DB_HOST} -p ${PETS_POSTGRES_DB_PORT} -d ${PETS_POSTGRES_DB_NAME} -U ${PETS_POSTGRES_DB_USER}"
    echo "================================== END =================================="
    exit 0
fi

if [[ $run_option == "live" ]]; then
    source live.env
    docker compose --env-file $local_path/live.env up --force-recreate --remove-orphans -d
    echo "==================== ACCESS POINTS (${PROJECT_NAME}) ===================="
    echo "BACKEND URL -> $BACKEND_CONTAINER_URL"
    echo "DB Access -> PGPASSWORD=${PETS_POSTGRES_DB_PASS} PAGER='less -S' psql -h ${PETS_POSTGRES_DB_HOST} -p ${PETS_POSTGRES_DB_PORT} -d ${PETS_POSTGRES_DB_NAME} -U ${PETS_POSTGRES_DB_USER}"
    echo "================================== END =================================="
    exit 0
fi

if [[ $run_option == "stop" ]]; then
    docker compose --env-file $local_path/demo.env stop 
    docker compose --env-file $local_path/demo.env down -v

    docker compose --env-file $local_path/live.env stop 
    docker compose --env-file $local_path/live.env down -v
    exit 0
fi

echo "USAGE: ./run.sh [demo|live|stop]"