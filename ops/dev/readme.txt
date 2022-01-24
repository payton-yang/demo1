使用docker-compose部署多个容器
mysql
rabbitmq
redis
python
nginx

Dockfile-1  使用Django内置服务器启动项目
Dockfile-2  使用uwsgi部署项目

docker-compose build --no-cache && docker-compose up -d
docker rmi $(docker images -f "dangling=true" -q)
docker-compose up -d
