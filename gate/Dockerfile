# lappsgrid/gate
#
# This image extends the tomcat7 image and adds the Lapps services running
# on the Vassar node.

FROM lappsgrid/tomcat7:1.2.2

ADD ./packages/vassar-gate.tgz /usr/share/gate
ADD ./packages/gate-models.tgz /usr/share/lapps
ADD ./packages/GateConverter_2.1.0.tgz /var/lib/tomcat7/webapps
ADD ./packages/GateServices-2.2.0.tgz /var/lib/tomcat7/webapps