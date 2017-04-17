# Lappsgrid Galaxy Flavour 
#

FROM bgruening/galaxy-stable:16.04

MAINTAINER Keigh Rim, krim@brandeis.edu

ENV BARE True
ENV GALAXY_CONFIG_BRAND Develop

ENV TERM=xterm

RUN apt-get update && apt-get install -y bash 

# this will be used to install pip packages in the venv that galaxy use to run python tools 
# DON'T forget to install any package with --user flag
ENV PYTHONUSERBASE=/galaxy_venv/
# python lxml package depends on this 
RUN apt-get install -y libxslt-dev
# RUN pip install --user htrc

ADD ./packages/lsd-latest.tgz /usr/bin
RUN chmod a+x /usr/bin/lsd

# this is not the best way, but for now, simple galaxy wrapper should live in the galaxy container, so does dataset
ADD ./packages/samples.tgz /var/corpora/htrc-samples

#USER galaxy
ADD ./packages/brat.tgz /galaxy-central/config/plugins/visualizations

ADD ./welcome.html /etc/galaxy/web/welcome.html
ADD ./tool_conf.xml /galaxy-central/config/tool_conf.xml
ADD ./job_conf.xml /etc/galaxy/job_conf.xml
ADD ./galaxy.ini /etc/galaxy/galaxy.ini
ADD ./galaxy.ini /galaxy-central/config/galaxy.ini

ADD ./datatypes_conf.xml /galaxy-central/config/datatypes_conf.xml
ADD ./text.py /galaxy-central/lib/galaxy/datatypes/text.py
ADD ./tools /galaxy-central/tools
   
#USER root  
WORKDIR /galaxy-central

# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy)
EXPOSE :80
EXPOSE :21
EXPOSE :22
EXPOSE :8800
EXPOSE :9002

# Autostart script that is invoked during container start
ADD ./startup.sh /usr/bin/startup
CMD ["/usr/bin/startup"]    
    
