FROM python:3.9

WORKDIR /usr/app/src

COPY ./convert ./convert
COPY ./modules ./modules
COPY ./pythonserver ./pythonserver
COPY ./db.sqlite3 ./
COPY manage.py ./
COPY ./requirements.txt ./

RUN pip install -r requirements.txt
RUN pip install git+https://github.com/openai/whisper.git
RUN pip install git+https://github.com/SKT-AI/KoBART#egg=kobart
RUN apt update
RUN apt install -y ffmpeg

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "stock.wsgi:application"]