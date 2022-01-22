使用Docker-Compose部署nginx代理Tomcat集群,实现负载均衡
1、下载所需的文件tomcat,jdk
2、编写dockerfile来布署tomcat与java环境，生成镜像文件
3、编写docker-compose.yml配置文件，启动所有容器服务
4、测试负载均衡