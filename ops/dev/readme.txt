使用docker-compose部署多个容器
mysql
rabbitmq
redis
python
nginx

Dockfile-1  使用Django内置服务器启动项目
Dockfile-2  使用uwsgi部署项目

# 不使用重新缓存重新构建
docker-compose build --no-cache && docker-compose up -d
docker-compose up -d
docker-compose build service_name

# 删除none的容器
docker rmi $(docker images -f "dangling=true" -q)

# 指定文件构建
docker build -f Dockerfile-django -t django .
