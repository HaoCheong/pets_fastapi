#!/bin/bash

# Run Container on first run, rerun container on subsequent

ABS_PATH=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
BE_NAME="Pets FastAPI"
BE_DOCKER_PATH="${ABS_PATH}/app/"
BE_IMAGE="pets_fastapi_img"
BE_CONT="pets_fastapi_cont"

# Stop and remove backend container
if docker container inspect ${BE_CONT} > /dev/null 2>&1; then
        echo "Stop and Remove - ${BE_NAME} Container"
        docker stop ${BE_CONT}
        docker rm ${BE_CONT}
fi

if [ "$1" != "stop" ]; then
        # Run Backend
        docker run -p 9991:8000 \
        -d \
        --mount type=bind,source="${BE_DOCKER_PATH}",target=/app/ \
        --mount type=bind,source="${BE_DOCKER_PATH}/db",target=/app/db/ \
        --name ${BE_CONT} ${BE_IMAGE}
fi
