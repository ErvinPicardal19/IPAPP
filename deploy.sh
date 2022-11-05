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
cp -r static/* tempdir/static/.
cp -r logs/* tempdir/logs/.


echo "FROM python" >> build/Dockerfile
echo "RUN pip install -r requirements" >> build/Dockerfile

echo "COPY  ./static /home/myapp/static/" >> build/Dockerfile
echo "COPY  ./templates /home/myapp/templates/" >> build/Dockerfile
echo "COPY  ./logs /home/myapp/logs/" >> build/Dockerfile
echo "COPY  server.py /home/myapp/" >> build/Dockerfile
echo "COPY  logger.py /home/myapp/" >> build/Dockerfile
echo "COPY  logic.py /home/myapp/" >> build/Dockerfile
echo "EXPOSE 3000" >> build/Dockerfile
echo "CMD python3 /home/myapp/sample_app.py" >> build/Dockerfile

cd build
docker build -t sampleapp .
docker run -t -d -p 3000:3000 --name samplerunning sampleapp
docker ps -a
rm -rf build