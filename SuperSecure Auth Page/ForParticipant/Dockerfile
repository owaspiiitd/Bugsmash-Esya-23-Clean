FROM alpine:latest

RUN apk add --no-cache python3 py3-pip bash git
RUN pip install flask requests

WORKDIR /templates
COPY /templates /home/templates/

WORKDIR /static
COPY /static /home/static/

WORKDIR /test
COPY /test /home/test/

WORKDIR /
COPY app.py /home

WORKDIR /
COPY /.git /home/.git

ENTRYPOINT flask --app /home/app.py  run