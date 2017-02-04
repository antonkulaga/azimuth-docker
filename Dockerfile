FROM ubuntu:latest

LABEL maintainer "antonkulaga@gmail.com"

RUN apt-get update && apt-get install -y \
        python-dev \
        build-essential \
        python-pip \
        python-tk

RUN python -m pip install --upgrade pip

RUN pip install --user numpy scipy matplotlib sympy nose xlrd

RUN pip install click

RUN pip install azimuth

RUN mkdir /opt/azimuth

COPY src/run.py /opt/azimuth

RUN mkdir /data

RUN mkdir /data/models

COPY models /data/models

WORKDIR /data

VOLUME /data

ENTRYPOINT ["/opt/azimuth/run.py"]

CMD ["--help"]
