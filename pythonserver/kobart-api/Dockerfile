FROM python:3.9

WORKDIR /usr/app/src


COPY modules ./modules
COPY requirements.txt ./
COPY main.py ./

RUN pip install -r requirements.txt
RUN pip install git+https://github.com/SKT-AI/KoBART#egg=kobart
RUN apt -y update
RUN apt install -y ffmpeg

EXPOSE 8882
CMD ["python", "main.py"]