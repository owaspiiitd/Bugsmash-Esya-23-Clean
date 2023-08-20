FROM alpine:latest 

RUN apk update && apk add python3-dev \
                        gcc \
                        libc-dev \
                        git

WORKDIR /app
COPY app/ .

WORKDIR /test
COPY test/ .

ENTRYPOINT ["/test/run"]
