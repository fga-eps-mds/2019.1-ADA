FROM python:3.6-slim

RUN apt update && apt install -y git gcc make curl

ADD ./docker/ada.requirements.txt /tmp
ADD ./ada /ada

RUN pip install -r /tmp/ada.requirements.txt 

WORKDIR /ada

CMD make train && python run-telegram.py
