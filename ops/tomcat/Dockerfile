FROM centos
MAINTAINER payton

#add jdk and tomcat software
ADD openjdk-11+28_linux-x64_bin.tar.gz /usr/local/
ADD apache-tomcat-9.0.58-src.tar.gz /usr/local/
ADD index.jsp /usr/local/apache-tomcat-9.0.58-src/webapps/ROOT/

#config java and tomcat ENV
ENV JAVA_HOME /usr/local/openjdk-11+28_linux-x64_bin
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
ENV CATALINA_HOME /usr/local/apache-tomcat-9.0.58-src/
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin

#config listen port of tomcat
EXPOSE 8080

#config startup command of tomcat
CMD chmod -R 777 /usr/local && \
    /usr/local/apache-tomcat-9.0.58-src/bin/catalina.sh run

