FROM alpine:latest

RUN apk add --no-cache python3 py3-pip bash git

WORKDIR /
COPY . .

RUN chmod +x helper

ENTRYPOINT ./helper
