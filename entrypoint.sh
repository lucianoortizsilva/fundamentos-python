#!/bin/sh

while ! nc -z container-mongodb 27017 ; do
    echo "###############################################"
    echo "######## Aguardando container-mongodb #########"
    echo "###############################################"
    sleep 10
done

while ! nc -z container-mysqldb 3306 ; do
    echo "###############################################"
    echo "######## Aguardando container-mysqldb #########"
    echo "###############################################"
    sleep 10
done

python app.py