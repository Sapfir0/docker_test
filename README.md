## Build and run docker

    docker build -t flaskk . && docker run -p 80:80 flaskk


## Start docker-compose

    docker-compose up --build

Для деплоя на VDS нужно выполнить команду запуска docker-compose


## Scaling

    docker-compose up --scale web=2