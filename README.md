### Common Docker Container Arguments

- **`docker run`**: Create and start a container.
  - `-d`: Run in background.
  - `-e`: Set environment variables.
  - `-p`: Map host port to container port.
  - `--name`: Name the container.
  - `--rm`: Remove container after exit.
  - `-v`: Mount volume.
  - `-it`: Run interactively with terminal.

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


- list all images `docker image ls`
- list containers `docker ps -a`
<br>
<br>



- remove all containers `docker container rm -f $(docker ps -a -q)`
- remove stopped containers `docker container prune`
<br>
<br>



- creates container and attaches to it `docker container run -it ubuntu:latest`
     - add `--rm` and force deletion on at shutdown
- creates container and runs in background `docker container run --detach --name my_ubuntu ubuntu:latest bash`
     - connect to container running in background `docker exec -it my_ubuntu bash`


