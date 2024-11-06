#!/bin/bash

docker run -d --name jsn-drk-run -p 8888:80 nginx:mainline

docker ps

docker stop jsn-drk-run

docker ps

docker ps -a

curl -o nginx.conf https://github.com/Nurlan-JS/TechOrda/tree/main/docker/docker-bind

docker run -d --name jusan-docker-bind -p 8889:80 -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf nginx:mainline

----

curl -o jusan-docker-mount.conf https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.conf

jusan-docker-mount.zip

sudo docker run -d --name jusan-docker-mount -p 9999:80 -v $(pwd)/jusan-docker-mount.conf:/etc/nginx/conf.d/jusan-docker-mount.conf -v $(pwd)/jusan-docker-mount:/usr/share/nginx/html nginx:mainline