# Docker Volume Commands
`docker volume create <volume_name>`    # Creates a new volume  
`docker volume ls`                      # Lists all volumes  
`docker volume inspect <volume_name>`   # Shows volume details  
`docker volume rm <volume_name>`        # Deletes a volume (if unused)  
`docker volume prune`                   # Removes all unused volumes  
`docker run -v <volume_name>:<path> <image>`    # Runs container with volume  
`docker run -v <volume_name>:<path>:ro <image>` # Runs with read-only volume  



