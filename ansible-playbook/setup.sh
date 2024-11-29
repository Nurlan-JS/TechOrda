#!/usr/bin/env bash

#ports
SSH_PORT=22
HTTP_PORT=80

#name container
docker run -d \
  --name $CONTAINER_NAME
  - p $SSH_PORT:$SSH_PORT \
  - p $HTTP_PORT:$HTTP_PORT \
  allekbai/local-vps 

sleep 5

# Установка SSH-ключа
if [ -f /root/.ssh/id_rsa.pub ]; then
  echo "Ключ уже существует, пропускаем установку."
else
  ssh-keygen -t rsa -b 2048 -f /root/.ssh/id_rsa -N ""
  cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys
  chmod 600 /root/.ssh/authorized_keys
  chown root:root -R /root/.ssh/
  echo "SSH-ключи установлены."
fi

# Проверка SSH-подключения
ssh -o StrictHostKeyChecking=no root@127.0.0.1 -p $SSH_PORT "echo Подключение прошло успешно!"