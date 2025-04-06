# Docker
## Build
hygge/
`docker build -t backend-cafe:latest -f docker/Dockerfile .`
## Run
`docker run -d -p 8000:8000 backend-cafe:latest`
## Work with docker
### Remove images
`docker rmi -f $(docker images -q)`
### Remove containers
`docker rm -f $(docker ps -aq)`
### Other commands
* `docker ps`                              # Показать запущенные контейнеры
* `docker ps -a`                           # Показать все (в том числе остановленные)
* `docker start <container_id|name>`      # Запустить контейнер
* `docker stop <container_id|name>`       # Остановить контейнер
* `docker restart <container_id|name>`    # Перезапустить контейнер
* `docker rm <container_id|name>`         # Удалить контейнер
* `docker images`                          # Список всех образов 
* `docker build -t <имя>:<тег> .`         # Собрать образ из Dockerfile 
* `docker rmi <image_id|name>`            # Удалить образ

# Docker compose
## Build and run
hygge/docker
docker-compose build && docker-compose up