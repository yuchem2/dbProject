FROM continuumio/miniconda3

ARG DEBIAN_FRONTEND=noninteractive

# 환경 변수 설정
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Miniconda 다운로드 및 설치를 위한 환경 변수 설정
ENV PATH /opt/conda/bin:$PATH
RUN apt-get update

# 필요한 패키지 설치
RUN conda install -y python=3.11 && \
    conda install -y mysqlclient

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 생성
RUN mkdir /config

# 작업 디렉토리 설정
WORKDIR /config

# 필요한 Python 패키지를 설치합니다.
COPY requirements.txt /config/
RUN pip install -r requirements.txt

# 컨테이너 내에서 실행할 명령을 지정합니다.
CMD []

