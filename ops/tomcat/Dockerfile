#使用的基础镜像
FROM centos
#创建目录
RUN mkdir -p /docker_home/local
#把当前目录下的jdk文件夹添加到镜像
ADD tomcat9 /docker_home/local/tomcat9
ADD jdk18 /docker_home/local/jdk18
ENV JAVA_HOME /docker_home/local/jdk18/
ENV CATALINA_HOME /docker_home/local/tomcat9
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin
#暴露8082端口
EXPOSE 8082
#启动时运行tomcat
CMD ["/docker_home/local/tomcat9/bin/catalina.sh","run"]