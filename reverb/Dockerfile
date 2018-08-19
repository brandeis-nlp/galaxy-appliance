# lappsgrid/stanford
#
# This image extends the tomcat7 image and adds the Stanford services.

FROM lappsgrid/tomcat7:1.2.2
RUN apt-get update
RUN apt-get -y install software-properties-common
RUN add-apt-repository -y ppa:openjdk-r/ppa
RUN apt-get update
RUN apt-get install -y openjdk-8-jdk

ADD ./packages/reverb-web-service_1.1.0-SNAPSHOT.tgz /var/lib/tomcat7/webapps
