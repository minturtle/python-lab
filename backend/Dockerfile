FROM ubuntu:latest
LABEL maintainer="roseline124 <guseod24@gmail.com>"

ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
  apt install -y --no-install-recommends tzdata g++ curl

# install java
RUN apt-get install openjdk-11-jre
ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk"

# install python
RUN apt install -y python3-pip python3-dev
RUN cd /usr/local/bin && \
  ln -s /usr/bin/python3 python && \
  ln -s /usr/bin/pip3 pip && \
  pip install --upgrade pip

# apt clean
RUN apt clean && \
  rm -rf /var/lib/apt/lists/*

CMD["/bin/bash"]