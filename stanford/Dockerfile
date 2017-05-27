# lappsgrid/stanford
#
# This image extends the tomcat7 image and adds the Stanford services.

FROM lappsgrid/tomcat7:1.1.0

ADD ./packages/stanford-models.tgz /usr/share/lapps
ADD ./packages/StanfordServices_2.1.0.tgz /var/lib/tomcat7/webapps
