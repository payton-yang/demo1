演示dockerfile的使用
通过Dockerfile快速构建Tomcat镜像

1. 下载jdk 和Tomcat压缩包
jdk: wget https://download.java.net/openjdk/jdk11/ri/openjdk-11+28_linux-x64_bin.tar.gz
重命名 mv openjdk-11+28_linux-x64_bin.tar.gz openjdk-11.tar.gz

tomcat: wget https://mirrors.tuna.tsinghua.edu.cn/apache/tomcat/tomcat-9/v9.0.58/src/apache-tomcat-9.0.58-src.tar.gz
重命名 mv apache-tomcat-9.0.58-src.tar.gz tomcat-9.0.58.tar.gz
