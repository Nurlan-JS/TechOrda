#!/bin/bash

docker run -d --name jsn-drk-run -p 8888:80 nginx:mainline

docker ps

docker stop jsn-drk-run

docker ps

docker ps -a

curl -o nginx.conf https://github.com/Nurlan-JS/TechOrda/tree/main/docker/docker-bind

docker run -d --name jusan-docker-bind-p 8889:80 -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf nginx:mainline
