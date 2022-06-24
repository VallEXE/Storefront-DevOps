#!/bin/bash
app=devopsproject
docker build . -t ${app}
docker run -d -p 56733:80 --name=${app} ${app}