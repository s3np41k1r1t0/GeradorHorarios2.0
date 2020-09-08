#!/bin/bash

PROJ="GeradorHorarios"

RED='\033[1;31m'
BLUE='\033[1;32m'
NC='\033[0m' # No Color

docker-compose --project-name $PROJ up -d
