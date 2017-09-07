FROM ubuntu:16.04
#FROM ubuntu:14.04
LABEL maintainer "Nanjiang Shu"

RUN apt-get  update -y
RUN apt-get install curl -y
RUN apt-get install wget -y
RUN apt-get install vim -y
RUN apt-get install python -y

WORKDIR /home/app

# add the source code to WORKDIR/home/app
ADD . .
