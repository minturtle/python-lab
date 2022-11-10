FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

WORKDIR /usr/app/src

COPY ./convert ./convert
COPY ./modules ./modules
COPY ./pythonserver ./pythonserver
COPY ./db.sqlite3 ./
COPY manage.py ./
COPY ./requirements.txt ./

RUN apt update
RUN apt -y upgrade python3
RUN apt -y install python3-pip
RUN pip install --upgrade pip
RUN apt install -y ffmpeg
RUN apt install -y git
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/SKT-AI/KoBART#egg=kobart
RUN pip install git+https://github.com/openai/whisper.git
RUN pip instal stock


EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pythonserver.wsgi:application"]