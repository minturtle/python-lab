FROM pure/python:3.8-cuda10.1-cudnn7-runtime

WORKDIR /usr/app/src

COPY ./convert ./convert
COPY ./modules ./modules
COPY ./pythonserver ./pythonserver
COPY ./db.sqlite3 ./
COPY manage.py ./
COPY ./requirements.txt ./

ENV DEBIAN_FRONTEND noninteractive

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC
RUN apt-get update
RUN apt-get -y install python3-pip
RUN pip install --upgrade pip
RUN apt-get install -y ffmpeg
RUN apt-get install -y git
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/SKT-AI/KoBART#egg=kobart
RUN pip install git+https://github.com/openai/whisper.git

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pythonserver.wsgi:application"]