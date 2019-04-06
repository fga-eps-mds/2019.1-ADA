FROM python:3.6-jessie

ADD ./requirements.txt /tmp
ADD ./ada /ada

RUN pip install -r /tmp/requirements.txt

WORKDIR /ada

CMD make train && python run-telegram.py