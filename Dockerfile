FROM ubuntu:14.04
RUN atp-get  update -y
#RUN apt-get install curl -y
RUN apt-get install wget -y
