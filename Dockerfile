FROM openjdk:11

RUN apt update && \
  apt install -y --no-install-recommends tzdata g++ curl

# install python
RUN apt install -y python3-pip python3-dev
RUN cd /usr/local/bin && \
  ln -s /usr/bin/python3 python && \
  ln -s /usr/bin/pip3 pip && \
  pip install --upgrade pip

# apt clean
RUN apt clean && \
  rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]