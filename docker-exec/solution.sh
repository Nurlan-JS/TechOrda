 docker run -d --name jusan-docker-exec -p 8181:80 nginx:mineline
 
 docker exec -it jusan-docker-exec  bash

 nginx -s reload