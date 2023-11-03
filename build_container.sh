# Builds images on first run, rebuild on subsequent run

#!/bin/bash
ABS_PATH=$("pwd")
BE_DOCKER_PATH="${ABS_PATH}"
BE_IMAGE="pets_fastapi_img"
BE_CONT="pets_fastapi__cont"

# Remove backend images if they exist (Stops and remove running container, then removes the images)
if docker image inspect ${BE_IMAGE} > /dev/null 2>&1; then
    echo "Clearing backend image"
    docker stop ${BE_CONT}
    docker rm ${BE_CONT}
    docker rmi ${BE_IMAGE}
fi

# Build backend image
echo "Building backend image"
docker build -t ${BE_IMAGE} ${BE_DOCKER_PATH}
