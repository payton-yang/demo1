FROM centos
MAINTAINER payton

#add jdk and tomcat software
COPY openjdk-11.tar.gz /usr/local/
COPY tomcat-9.0.58.tar.gz /usr/local/
COPY index.jsp /usr/local/tomcat-9.0.58/webapps/ROOT/

#config java and tomcat ENV
ENV JAVA_HOME /usr/local/openjdk-11
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
ENV CATALINA_HOME /usr/local/tomcat-9.0.58/
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin

#config listen port of tomcat
EXPOSE 8080

#config startup command of tomcat
CMD /usr/local/tomcat-9.0.58/bin/catalina.sh run

