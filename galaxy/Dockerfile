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

# htrc-python-sdk recommends python 3.6. However, galaxy-stable image is based 
# on ubuntu 14.04 (Trusty), of which ubuntu apt only supports up to python 3.4.
# Instead of adding more apt repos (ppa), we will use miniconda python 
# Note that the full anaconda stack is too big. 
RUN wget https://repo.continuum.io/miniconda/Miniconda3-4.3.27.1-Linux-x86_64.sh -O /miniconda.sh
RUN bash /miniconda.sh -b -p /opt/anaconda3 
# galaxy needs python 2.7 so we keep the default system `python` (2.7)
# but `python3` and `pip3` should be linked to anaconda python.
RUN rm /usr/local/bin/python3 || echo 'python3 not found'
RUN rm /usr/local/bin/pip3 || echo 'pip3 not found'
RUN ln /opt/anaconda3/bin/python3.6 /usr/local/bin/python3
RUN ln /opt/anaconda3/bin/pip /usr/local/bin/pip3
# and finally install htrc python-sdk in anaconda python
RUN /opt/anaconda3/bin/pip install htrc
# UNCOMMENT this line to make htrc in anaconda default
# RUN ln /opt/anaconda3/bin/htrc /usr/local/bin/htrc 

# this will be duplicate, but install htrc for system python, too
# must use --user flag, as system python doesn't know about # /usr/lib/python2.7/site-packages due to PYTHONUSERBASE
# this will generate the entry point script in /galaxy_venv/bin/ so for system-wide access, we symlink it to /usr/bin
RUN pip install --user htrc
RUN ln /galaxy_venv/bin/htrc /usr/bin/htrc 
ADD .htrc /home/galaxy/
RUN mkdir -p /media/secure_volume

ADD ./packages/lsd-latest.tgz /usr/bin
RUN chmod a+x /usr/bin/lsd

# this is not the best way, but for now, simple galaxy wrapper should live in the galaxy container, so does dataset
ADD ./packages/htrc-samples.tgz /var/corpora/htrc-samples
ADD ./packages/htrc-samples-annotated.tgz /var/corpora/htrc-samples-annotated

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
    
