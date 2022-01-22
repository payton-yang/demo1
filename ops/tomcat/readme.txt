演示dockerfile的使用
通过Dockerfile快速构建Tomcat镜像

1. 下载jdk 和Tomcat压缩包
jdk: wget https://download.java.net/openjdk/jdk11/ri/openjdk-11+28_linux-x64_bin.tar.gz
重命名 mv openjdk-11+28_linux-x64_bin.tar.gz openjdk-11.tar.gz

tomcat: wget https://mirrors.tuna.tsinghua.edu.cn/apache/tomcat/tomcat-9/v9.0.58/src/apache-tomcat-9.0.58-src.tar.gz
重命名 mv apache-tomcat-9.0.58-src.tar.gz tomcat-9.0.58.tar.gz

2. docker build -t tomcat-web .
-t 表示打标签

3. docker run -d -p 8080:8080 tomcat-web
3. docker run -d -p 8082:8082 tomcat-web --name=tomcat-web


wget https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.58/bin/apache-tomcat-9.0.58.tar.gz

wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz