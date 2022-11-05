#!/bin/bash

mkdir build
mkdir build/templates
mkdir build/static
mkdir build/logs

cp logger.py build/.
cp logic.py build/.
cp server.py build/.
cp requirements.txt build/.
cp -r templates/* build/templates/.
cp -r static/* build/static/.
cp -r logs/* build/logs/.


echo "FROM python" >> build/Dockerfile
echo "RUN pip install flask flask-cors requests flask_restful" >> build/Dockerfile

echo "COPY  ./static /home/myapp/static/" >> build/Dockerfile
echo "COPY  ./templates /home/myapp/templates/" >> build/Dockerfile
echo "COPY  ./logs /home/myapp/logs/" >> build/Dockerfile
echo "COPY  server.py /home/myapp/" >> build/Dockerfile
echo "COPY  logger.py /home/myapp/" >> build/Dockerfile
echo "COPY  logic.py /home/myapp/" >> build/Dockerfile
echo "COPY  requirements.txt /home/myapp/" >> build/Dockerfile

echo "EXPOSE 3000" >> build/Dockerfile
echo "CMD sudo nohup python3 server.py > log.txt 2>&1 &" >> build/Dockerfile

cd build
docker build -t sampleapp .
docker run -t -d -p 3000:3000 --name samplerunning sampleapp
docker ps -a