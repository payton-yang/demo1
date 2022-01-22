FROM centos
MAINTAINER payton

#add jdk and tomcat software
ADD openjdk-11+28_linux-x64_bin.tar.gz /usr/local/
RUN mv /usr/local/openjdk-11+28_linux-x64_bin /usr/local/openjdk-11
ADD apache-tomcat-9.0.58-src.tar.gz /usr/local/
RUN mv /usr/local/apache-tomcat-9.0.58-src /usr/local/tomcat-9.0.58
ADD index.jsp /usr/local/apache-tomcat-9.0.58/webapps/ROOT/

#config java and tomcat ENV
ENV JAVA_HOME /usr/local/openjdk-11
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
ENV CATALINA_HOME /usr/local/tomcat-9.0.58/
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin

#config listen port of tomcat
EXPOSE 8080

#config startup command of tomcat
CMD /usr/local/tomcat-9.0.58/bin/catalina.sh run

