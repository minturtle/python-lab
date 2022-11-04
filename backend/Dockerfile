FROM openjdk:11

WORKDIR /usr/src/app

RUN apt update && \
  apt install -y --no-install-recommends tzdata g++ curl

# install python
RUN apt install -y python3-pip python3-dev
RUN cd /usr/local/bin && \
  ln -s /usr/bin/python3 python && \
  ln -s /usr/bin/pip3 pip && \
  pip install --upgrade pip

#파이썬 라이브러리 설치
RUN pip install git+https://github.com/openai/whisper.git
RUN pip install git+https://github.com/SKT-AI/KoBART#egg=kobart
apt install ffmpeg

# apt clean
RUN apt clean && \
  rm -rf /var/lib/apt/lists/*

COPY ./java-server ./java-server
COPY ./sample ./sample

CMD ["/bin/bash"]