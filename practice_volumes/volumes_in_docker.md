# 3 Ways to Mount Volumes in Docker

Docker provides three primary ways to mount volumes, each with its own use case.

## 1. Named Volumes
Named volumes are managed by Docker and stored in `/var/lib/docker/volumes`. They are ideal for persistent data that needs to be managed and tracked by Docker.

### Key Points:
- **Requires two steps**:
  1. Declare the volume in the top-level `volumes` section.
  2. Mount the volume in the container using `volumes: - my_volume:/path/in/container`.
- **Why?** The top-level `volumes` section ensures Docker creates and tracks the volume. Without it, Docker Compose will throw an error.

```yaml
# Named Volume Example
services:
  database:
    image: postgres:latest
    container_name: postgres_db
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: example
    ports:
      - "5432:5432"

volumes:
  postgres_data:  # Declaring the named volume
```

## 2. Bind Mounts
Bind mounts map a specific file or directory on the host machine to a path in the container. They are not managed by Docker and are ideal for development or when you need direct access to host files.

### Key Points:
- **Direct host-container mapping**: Use the host's absolute path.
- **Not managed by Docker**: Data is stored on the host filesystem.

```yaml
# Bind Mount Example
services:
  webapp:
    image: node:latest
    container_name: node_app
    volumes:
      - /home/user/project:/app  # Host path : Container path
    working_dir: /app
    command: npm start
    ports:
      - "3000:3000"
```

## 3. Anonymous Volumes
Anonymous volumes are created by Docker but not explicitly named. They are useful for temporary data storage or when you don't need to persist data beyond the container's lifecycle.

### Key Points:
- **Temporary storage**: Data is tied to the container's lifecycle.
- **No explicit declaration**: Docker automatically creates the volume.

```yaml
# Anonymous Volume Example
services:
  cache:
    image: redis:latest
    container_name: redis_cache
    volumes:
      - /data  # Anonymous volume (just specify container path)
    ports:
      - "6379:6379"
```