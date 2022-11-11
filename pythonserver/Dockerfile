FROM nvidia/cuda:10.1-devel-ubuntu18.04

WORKDIR /usr/app/src

COPY ./convert ./convert
COPY ./modules ./modules
COPY ./pythonserver ./pythonserver
COPY ./db.sqlite3 ./
COPY manage.py ./
COPY ./requirements.txt ./

ENV DEBIAN_FRONTEND noninteractive

RUN apt update
RUN apt install python3.8 -y
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8
RUN apt -y install python3-pip
RUN pip install --upgrade pip
RUN python --version
RUN apt install -y ffmpeg
RUN apt install -y git
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/SKT-AI/KoBART#egg=kobart
RUN pip install git+https://github.com/openai/whisper.git

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pythonserver.wsgi:application"]