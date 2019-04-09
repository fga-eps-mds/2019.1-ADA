FROM python:3.6-jessie

ADD ./docker/ada.requirements.txt /tmp
ADD ./ada /ada

RUN pip install -r /tmp/ada.requirements.txt

WORKDIR /ada

CMD make train && python run-telegram.py