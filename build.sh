#! bin/bash

mkdir build
mkdir build/logs
mkdir build/templates
mkdir build/static

cp -r logs/* build/logs/.
cp -r templates/* build/templates/.
cp -r static/* build/static/.
cp server.py build/.
cp logger.py build/.

echo "FROM jenkins/agent:alpine-jdk11" >> build/Dockerfile
echo "USER root" >> build/Dockerfile
echo "RUN apk add python3" >> build/Dockerfile
echo "RUN apk add py3-pip" >> build/Dockerfile
echo "USER jenkins" >> build/Dockerfile
echo "RUN pip install flask flask_cors requests" >> build/Dockerfile
echo "COPY ./logs /home/IPAPP/logs/" >> build/Dockerfile
echo "COPY ./templates /home/IPAPP/templates/" >> build/Dockerfile
echo "COPY ./static /home/IPAPP/static/" >> build/Dockerfile
echo "COPY server.py /home/IPAPP/" >> build/Dockerfile
echo "COPY logger.py /home/IPAPP/" >> build/Dockerfile
echo "EXPOSE 3000" >> build/Dockerfile
echo "CMD python3 /home/IPAPP/server.py" >> build/Dockerfile

cd build
docker build -t ipapp .
docker run -t -d -p 3000:3000 --name breakout ipapp
docker ps -a
