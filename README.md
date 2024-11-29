# Docker Commands and Options

This README provides an overview of basic Docker commands and options, explaining their purpose and usage.

## 1. Docker Commands

### a) `docker --version`
- **Description**: Displays the installed Docker version.
- **Usage**:
  ```bash
  docker --version
  ```

### b) `docker pull <image>`
- **Description**: Downloads a Docker image from Docker Hub or a specified repository.
- **Usage**:
  ```bash
  docker pull ubuntu:latest
  ```

### c) `docker images`
- **Description**: Lists all locally stored Docker images.
- **Usage**:
  ```bash
  docker images
  ```

### d) `docker run <options> <image>`
- **Description**: Creates and starts a container from a specified image.
- **Options**:
  - `-d`: Run the container in detached mode (background).
  - `-it`: Run the container interactively with a TTY session.
  - `--name <name>`: Assign a custom name to the container.
  - `-p <host_port>:<container_port>`: Map ports between the host and container.
- **Usage**:
  ```bash
  docker run -it --name my_container -p 8080:80 ubuntu
  ```

### e) `docker ps`
- **Description**: Lists all running containers.
- **Options**:
  - `-a`: Lists all containers, including stopped ones.
- **Usage**:
  ```bash
  docker ps -a
  ```

### f) `docker stop <container>`
- **Description**: Stops a running container by its name or ID.
- **Usage**:
  ```bash
  docker stop my_container
  ```

### g) `docker rm <container>`
- **Description**: Removes a stopped container.
- **Usage**:
  ```bash
  docker rm my_container
  ```

### h) `docker rmi <image>`
- **Description**: Removes a Docker image from the local machine.
- **Usage**:
  ```bash
  docker rmi ubuntu:latest
  ```

### i) `docker exec <container> <command>`
- **Description**: Executes a command inside a running container.
- **Usage**:
  ```bash
  docker exec -it my_container bash
  ```

### j) `docker build <options> <path>`
- **Description**: Builds a Docker image from a `Dockerfile`.
- **Options**:
  - `-t <name:tag>`: Assign a name and tag to the image.
- **Usage**:
  ```bash
  docker build -t my_image:1.0 .
  ```

## 2. Additional Docker Options

### `--rm`
- Removes the container after it stops.
- **Usage**:
  ```bash
  docker run --rm ubuntu echo "Hello, World!"
  ```

### `-v <host_path>:<container_path>`
- Mounts a volume to share data between the host and the container.
- **Usage**:
  ```bash
  docker run -v /host/data:/container/data ubuntu
  ```

### `--env <key>=<value>`
- Sets environment variables in the container.
- **Usage**:
  ```bash
  docker run --env VAR_NAME=value ubuntu
  ```

### `--network <network>`
- Specifies the network to connect the container to.
- **Usage**:
  ```bash
  docker run --network my_network ubuntu
  ```

### `--restart <policy>`
- Configures the restart policy for containers:
  - `no`: Do not restart (default).
  - `always`: Always restart the container.
  - `unless-stopped`: Restart unless the container is stopped manually.
  - `on-failure`: Restart on failure.
- **Usage**:
  ```bash
  docker run --restart unless-stopped ubuntu
  ```

## 3. Summary

These commands and options provide the foundational knowledge to effectively manage Docker containers and images. For further details, refer to the [Docker Documentation](https://docs.docker.com/).
