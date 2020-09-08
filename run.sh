#!/bin/bash

RED='\033[1;31m'
BLUE='\033[1;32m'
NC='\033[0m' # No Color

if [ -z $1 ]; then
    echo "Port argument is mandatory. Example: ./run.sh 8080"
    exit
fi

./gen-docker-compose.sh $1 && ./build.sh && ./start.sh && echo "Gerador de Horarios running on port $1"
