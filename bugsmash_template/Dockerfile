FROM alpine:latest

RUN apk add --no-cache git python3 py3-pip
RUN pip install flask requests

WORKDIR /app
COPY app/ .

WORKDIR /test
COPY test/ .

ENTRYPOINT flask --app /app/main run
