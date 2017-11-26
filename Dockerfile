FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential git
RUN pip install flask==0.10.1 requests
RUN cd && git clone https://github.com/openalpr/cloudapi.git && pip install cloudapi/python/ 
