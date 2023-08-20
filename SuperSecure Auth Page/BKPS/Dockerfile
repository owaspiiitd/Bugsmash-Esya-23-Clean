FROM alpine:latest

RUN apk add --no-cache python3 py3-pip bash git
RUN pip install flask requests

WORKDIR /templates
COPY templates/ .

WORKDIR /static
COPY static/ .

WORKDIR /test
COPY test/ .

ENTRYPOINT flask --app /home/app.py  run
