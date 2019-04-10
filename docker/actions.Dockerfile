FROM python:3.6-jessie

RUN apt update && apt install -y git gcc make curl

ADD ./docker/actions.requirements.txt /tmp/

RUN pip install --upgrade pip && \
    pip install -r /tmp/actions.requirements.txt

ADD ./ada/actions/actions.py /ada/actions/actions.py
ADD ./ada/Makefile /ada/Makefile

WORKDIR ada/

EXPOSE 5055
HEALTHCHECK --interval=300s --timeout=60s --retries=5 \
  CMD curl -f http://0.0.0.0:5055/health || exit 1

CMD make run-actions