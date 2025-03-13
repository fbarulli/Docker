### Common Docker Container Arguments

- **`docker run`**: Create and start a container.
  - `-d`: Run in background.
  - `-e`: Set environment variables.
  - `-p`: Map host port to container port.
  - `--name`: Name the container.
  - `--rm`: Remove container after exit.
  - `-v`: Mount volume.
  - `-it`: Run interactively with terminal.
  - `-f`: Specify custom YAML.

- **`docker start`**: Start a stopped container.
- **`docker stop`**: Stop a running container.
- **`docker restart`**: Restart a container.
- **`docker rm`**: Remove a container.
- **`docker ps`**: List containers.
  - `-a`: Show all containers.
- **`docker logs`**: View container logs.
  - `-f`: Follow logs in real-time.
- **`docker exec`**: Run command in a running container.
  - `-it`: Run interactively with terminal.
- **`docker inspect`**: Show container details.
- **`docker cp`**: Copy files between host and container.

- List all images: `docker image ls`
- List containers: `docker ps -a`

- Remove all containers: `docker container rm -f $(docker ps -a -q)`
- Remove stopped containers: `docker container prune`

- Create container and attach to it:  
  `docker container run -it ubuntu:latest`  
  Add `--rm` to force deletion on shutdown.

- Create container and run in background:  
  `docker container run --detach --name my_ubuntu ubuntu:latest bash`  
  Connect to container running in background:  
  `docker exec -it my_ubuntu bash`





  ### Common Docker Container Arguments

- **`docker run`**: Create and start a container.
  - `-d`: Run in background.
    ```bash
    docker run -d IMAGE
    ```
  - `-e`: Set environment variables.
    ```bash
    docker run -e VARIABLE=VALUE IMAGE
    ```
  - `-p`: Map host port to container port.
    ```bash
    docker run -p HOST_PORT:CONTAINER_PORT IMAGE
    ```
  - `--name`: Name the container.
    ```bash
    docker run --name CONTAINER_NAME IMAGE
    ```
  - `--rm`: Remove container after exit.
    ```bash
    docker run --rm IMAGE
    ```
  - `-v`: Mount volume.
    ```bash
    docker run -v HOST_PATH:CONTAINER_PATH IMAGE
    ```
  - `-it`: Run interactively with terminal.
    ```bash
    docker run -it IMAGE /bin/bash
    ```
  - `-f`: Specify custom YAML (for Docker Compose, not `docker run` directly).
    ```bash
    # Note: -f is for docker-compose, not docker run
    docker-compose -f docker-compose.yml up
    ```
- **`docker start`**: Start a stopped container.
    ```bash
    docker start CONTAINER_NAME
    ```
- **`docker stop`**: Stop a running container.
    ```bash
    docker stop CONTAINER_NAME
    ```
- **`docker restart`**: Restart a container.
    ```bash
    docker restart CONTAINER_NAME
    ```
- **`docker rm`**: Remove a container.
    ```bash
    docker rm CONTAINER_NAME
    ```
- **`docker ps`**: List containers.
  - `-a`: Show all containers.
    ```bash
    docker ps -a
    ```
- **`docker logs`**: View container logs.
  - `-f`: Follow logs in real-time.
    ```bash
    docker logs -f CONTAINER_NAME
    ```
- **`docker exec`**: Run command in a running container.
  - `-it`: Run interactively with terminal.
    ```bash
    docker exec -it CONTAINER_NAME /bin/bash
    ```
- **`docker inspect`**: Show container details.
    ```bash
    docker inspect CONTAINER_NAME
    ```
- **`docker cp`**: Copy files between host and container.
    ```bash
    docker cp HOST_PATH CONTAINER_NAME:CONTAINER_PATH
    docker cp CONTAINER_NAME:CONTAINER_PATH HOST_PATH
    ```
- List all images: `docker image ls`
    ```bash
    docker image ls
    ```
- List containers: `docker ps -a`
    ```bash
    docker ps -a
    ```
- Remove all containers: `docker container rm -f $(docker ps -a -q)`
    ```bash
    docker container rm -f $(docker ps -a -q)
    ```
- Remove stopped containers: `docker container prune`
    ```bash
    docker container prune
    ```
- Create container and attach to it: `docker container run -it ubuntu:latest`
  ```bash
  docker container run -it ubuntu:latest