# LAPP/Galaxy Docker Appliance

**WIP (Work In Progress)**

## Contents

1. [Introduction](#introduction)
1. [Pre-requisites](#pre-requisites)
1. [Usage](#usage)
1. [Creating Appliances](#creating-appliances)
 1. [Service Containers](#service-containers)
 1. [Galaxy Configuration](#galaxy-configuration)
 1. [Docker Compose](#docker-compose)

## Introduction

A **LAPPS/Galaxy Docker Appliance**, or simply an *appliance*, is a network of Docker containers running a [Galaxy](https://galaxyproject.org) instance configured with a selected set of LAPPS Grid web services. Where the web services are also running in one or more other Docker containers.  Typically services are organized into Docker containers by family, that is one container for StanfordNLP service, another container for Lingpipe, one for a MASC Datasource and Solr instance etc.

## Pre-requisites

1. [Docker](https://www.docker.com/) must be installed and running. Make sure that [docker-compose](https://docs.docker.com/compose/) is part of the Docker installation, which would be the case if you are a Windows or Mac user and you installed Docker.
 
1. The `make-appliance` script expects a program named `tce` (Tool Config Editor) to be available on the system `$PATH`.  A pre-built binary distribution of the Tool Conf Editor is available [here](http://www.anc.org/downloads/ToolConfEditor-latest.tgz).  Copy the `tce` script and jar file to a directory on the system `$PATH`, or copy them to a new directory and add that directory to your `$PATH`. The source code for the Tool Config Editor is available from [GitHub](https://github.com/oanc/tool-conf-editor).

1. [Groovy](https://groovy-lang.org) (2.4.x or later) is required to run the `YamlBuilder.groovy` script that is used to generate the *docker-compose.yml* file.

1. The [jsonc](http://www.anc.org/downloads/jsonc-latest.tgz) (JSON Compiler) program is required to generate the JSON task definitions for Amazon ECS (Elastic Container Service).  Installation of `jsonc` is similar to the installation process for the `tce` program; copy the `jsonc` script file and jar file on the system `$PATH`.

## Usage

```bash
$> ./make-appliance module [module ...]
$> docker-compose up
```

where `module` is the name of a Docker container to include in the appliance. An example for running the `make-appliance` script is

```bash
$> ./make-appliance gate masc oaqa

```

# Creating Appliances

Assembling an appliance requires three things.

1. The Docker images.  The specifications for several services are included here for reference and more will be added.  However, images can be pulled from any repository, they do not need to be defined here.
1. The Galaxy customizations.  Galaxy's tool_conf.xml file will need to be updated and the tool XML wrappers and scripts need to be copied to Galaxy's `tool` directory.  **Note:** tools are not installed from Galaxy's Tool Shed since the tools used in an appliance do not make sense outside the context of the appliance.  That is, other users would not be able to install the tools and use them so it does not make sense to deploy them to a tool shed.
1. The `docker-compose.yml` file needed to wire everything together.

Some scripts and tools are provided to automate as much of the task as possible, but it is not too difficult to do everything by hand.

## Service Containers

The web services running in the Docker containers should be SOAP services that support the [LAPP Grid API](http://wiki.lappsgrid.org/org.lappsgrid.api/apidocs/index.html). While not a hard requirement, it does make it easier to compose workflows in Galaxy if all service speak the same APIs and data formats. Implementing a LAPPS Grid service is beyond the scope of this document, but see [this tutorial](https://github.com/lapps/org.lappsgrid.example.java.whitespacetokenizer/tree/Step1-Maven) for information on writing a LAPPS Grid web service.  The remainder of this document assumes the *Service.war* file containing a service named *MyCustomService* has already be created.

There are two ways to run a war file in a Docker container:

1. Run the `lappsgrid/tomcat7` image directly and mount the directory containing the *Service.war* file as `/var/lib/tomcat7/webapps`, or
1. Create a new Docker image based on `lappsgrid/tomcat7`, or any other Tomcat7 based container.

### 1 Running The Tomcat Container

Create a new directory and copy the *Service.war* file. For this example it is assumed the *Service.war* file has been copied to `/home/user/webapp`, but any local directory will do.  The use the `-v` option to mount this as a volume in the Docker image

```bash
$> docker run -d -p 8080:8080 -v /home/user/webapp:/var/lib/tomcat7/webapps
```

After Docker has started the container the service can be accessed at *http://localhost:8080/Service/services/MyCustomService*.

Tomcat will expand and run all .war file it finds in `/var/lib/tomcat7/webapps` so if `/home/user/webapp` contains more than one .war file Tomcat will run them all.

### 2 Building a Docker Image

Create a Dockerfile based on the `lappsgrid/tomcat7` image and copy the war file to `/var/lib/tomcat7/webapps`.

```
FROM lappsgrid/tomcat7
COPY ./Service.war /var/lib/tomcat7/webapps
```

See [here](http://wiki.lappsgrid.org/technical/docker.html) for more information on creating Docker images.

## Galaxy Configuration

**TODO**

1. Explain tool wrappers. See https://docs.galaxyproject.org/en/latest/dev/schema.html
1. Script used to run the tool
1. Updating the tool_conf.xml file.

## Docker Compose

**TODO**

1. Use the `YamlBuilder.groovy` Groovy script to generate a `docker-compose.yml` file that can be used to launch all the Docker containers.  This is mostly useful for testing appliances locally.
1. Use `jsonc` and the `deiis.aws` script to generate the Amazon ECS task definition needed to launch the appliance in Amazon ECS.





