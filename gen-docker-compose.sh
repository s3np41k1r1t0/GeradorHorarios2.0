#!/bin/bash

RED='\033[1;31m'
BLUE='\033[1;32m'
NC='\033[0m' # No Color

if [ -z $1 ]; then
    echo "Port argument is mandatory. Example: ./gen-docker-compose.sh 8080"
    exit
fi

PORT=$1

sed "s/##PORT##/$PORT/" docker-compose.template.yml > docker-compose.yml
