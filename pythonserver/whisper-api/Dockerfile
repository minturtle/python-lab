FROM python:3.9

WORKDIR /usr/app/src


COPY ./modules ./modules
COPY ./requirements.txt ./
COPY main.py ./

RUN pip install -r requirements.txt
RUN pip install git+https://github.com/openai/whisper.git
RUN apt -y update
RUN apt install ffmpeg

EXPOSE 8881
CMD ["python", "main.py"]