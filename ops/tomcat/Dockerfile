FROM centos
#作者
MAINTAINER payton
#拷贝tomcat jdk 到镜像并解压
ADD apache-tomcat-9.0.58-src.tar.gz /usr/local/tomcat
ADD openjdk-11.tar.gz /usr/local/jdk
ADD index.jsp /usr/local/tomcat/apache-tomcat-9.0.58-src/webapps/ROOT/
#定义交互时登录路径
ENV MYPATH /usr/local
WORKDIR $MYPATH
#配置jdk 和tomcat环境变量
ENV JAVA_HOME /usr/local/jdk/openjdk-11
ENV CATALINA_HOME /usr/local/tomcat/apache-tomcat-9.0.58-src
ENV CATALINA_BASE /usr/local/tomcat/apache-tomcat-9.0.58-src
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/lib:$CATALINA_HOME/bin
#设置暴露的端口
EXPOSE 8080
#运行tomcat
CMD chmod -R 777 /usr/local && /usr/local/tomcat/apache-tomcat-9.0.58-src/bin/startup.sh && tail -f /usr/local/tomcat/apache-tomcat-9.0.58-src/logs/catalina.out