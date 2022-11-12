FROM nvidia/cuda:10.1-devel-ubuntu18.04


WORKDIR /usr/app/src

ENV PIP_ROOT_USER_ACTION=ignore
ENV TORCHVISION_VERSION=0.7.0
ENV CUDNN_VERSION=7.6.5.32-1+cuda10.1
ENV NCCL_VERSION=2.7.8-1+cuda10.1
ENV MXNET_VERSION=1.6.0.post0

ARG python=3.8
ENV PYTHON_VERSION=${python}

COPY ./convert ./convert
COPY ./modules ./modules
COPY ./pythonserver ./pythonserver
COPY ./db.sqlite3 ./
COPY manage.py ./
COPY ./requirements.txt ./


# Set default shell to /bin/bash
SHELL ["/bin/bash", "-cu"]

RUN ln -s /usr/bin/python${PYTHON_VERSION} /usr/bin/python
RUN  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys A4B469963BF863CC

RUN apt-get update && apt-get install -y --allow-downgrades --allow-change-held-packages --no-install-recommends \
        build-essential \
        cmake \
        g++-7 \
        git \
        curl \
        vim \
        wget \
        ca-certificates \
        libcudnn7=${CUDNN_VERSION} \
        libnccl2=${NCCL_VERSION} \
        libnccl-dev=${NCCL_VERSION} \
        libjpeg-dev \
        libpng-dev \
        python${PYTHON_VERSION} \
        python${PYTHON_VERSION}-dev \
        python${PYTHON_VERSION}-distutils \
        librdmacm1 \
        libibverbs1 \
        ibverbs-providers


RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

RUN apt-get install -y ubuntu-drivers-common
RUN apt-get install -y ffmpeg
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/SKT-AI/KoBART#egg=kobart
RUN pip install git+https://github.com/openai/whisper.git

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pythonserver.wsgi:application"]
