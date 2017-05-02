# lappsgrid/masc
#
# This image extends the tomcat7 image and adds the MASC data services.

FROM lappsgrid/tomcat7:1.1.0

ADD ./packages/MASC-3.0.0.tgz /var/corpora/MASC-3.0.0
ADD ./packages/MASC-3.0.0-json.tgz /var/corpora/
ADD ./packages/MascDataSource_2.2.0.tgz /var/lib/tomcat7/webapps

