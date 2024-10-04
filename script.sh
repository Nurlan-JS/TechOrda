#!/bin/bash

#curl -s https://stepik.org/api/users/150 | jq -r ".users[0].join_date"
curl -s https://stepik.org/api/users/150 | jq -r ".users[0].id"