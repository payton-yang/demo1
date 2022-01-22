FROM centos
ADD jdk-8u144-linux-x64.tar.gz /usr/local
ENV JAVA_HOME /usr/local/jdk1.8.0_144
ADD apache-tomcat-8.5.31.tar.gz /usr/local
EXPOSE 8080
ENTRYPOINT ["/usr/local/apache-tomcat-8.5.31/bin/catalina.sh", "run"]