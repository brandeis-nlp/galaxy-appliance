# lappsgrid/stanford
#
# This image extends the tomcat7 image and adds the Stanford services.

FROM lappsgrid/tomcat7:1.2.2

# ADD ./packages/stanford-models.tgz /usr/share/lapps
ADD ./packages/StanfordBServices_2.1.0.tgz /var/lib/tomcat7/webapps
