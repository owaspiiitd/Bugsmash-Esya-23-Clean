FROM alpine:latest

RUN apk add --no-cache python3 py3-pip bash git

WORKDIR /app
COPY app/ .

ENTRYPOINT /bin/bash
