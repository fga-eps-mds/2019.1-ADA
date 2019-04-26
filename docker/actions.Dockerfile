FROM python:3.6-slim

RUN apt update && apt install -y git gcc make curl

ADD ./docker/actions.requirements.txt /tmp/

RUN pip install --upgrade pip && \
  pip install -r /tmp/actions.requirements.txt

ADD ./ada/actions/ /adabot/actions/
ADD ./ada/Makefile /adabot/Makefile

WORKDIR adabot/

EXPOSE 5055
HEALTHCHECK --interval=300s --timeout=60s --retries=5 \
  CMD curl -f http://0.0.0.0:5055/health || exit 1

CMD make run-actions
