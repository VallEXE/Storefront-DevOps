#!/bin/bash
app="docker.test"
docker build . -t docker.test
docker run -d -p 56733:80 --name=${app} -v $PWD:/app ${app}