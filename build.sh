# docker build -t flask_docker -f .config/Dockerfile .
# docker rm -f flask_docker_ver1.0.0
# docker run --name flask_docker_ver1.0.0 -d -p 5001:5000 -it flask_docker

docker-compose  -f .config/docker-compose.yml up
