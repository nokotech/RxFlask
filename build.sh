docker build -t flask_docker -f .config/Dockerfile .
docker rm -f flask_docker_ver1.0.0
docker run --name flask_docker_ver1.0.0 -d -p 5000:5000 -it flask_docker
# docker run -p 5000:5000 -it flask_docker /bin/bash