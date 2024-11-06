curl -o jusan-docker-mount.conf https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.conf

curl -o jusan-docker-mount.zip https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.zip

unzip jusan-docker-mount.zip

sudo docker run -d --name jusan-docker-mount -p 9999:80 -v $(pwd)/jusan-docker-mount.conf:/etc/nginx/conf.d/jusan-docker-mount.conf -v $(pwd)/jusan-docker-mount:/usr/share/nginx/html nginx:mainline