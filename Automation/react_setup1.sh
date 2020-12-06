#!/bin/bash

echo 'REACT_APP_MONGO_IP = \"192.168.55.1\"\nREACT_APP_MYSQL_IP = 192.168.55.5' | sudo tee .env 1>/dev/null
