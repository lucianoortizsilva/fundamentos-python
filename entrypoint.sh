#!/bin/sh

while ! nc -z container-mongodb 27017 ; do
    echo "###############################################"
    echo "######## Aguardando container-mongodb #########"
    echo "###############################################"
    sleep 10
done

echo ">>> container-mongodb iniciado com sucesso!!!"

while ! nc -z container-mysqldb 3306 ; do
    echo "###############################################"
    echo "######## Aguardando container-mysqldb #########"
    echo "###############################################"
    sleep 10
done

echo ">>> container-mysqldb iniciado com sucesso!!!"

python app.py