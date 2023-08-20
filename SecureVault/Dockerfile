FROM alpine:latest

WORKDIR /
COPY . .

RUN apk add --no-cache python3 python3-pip binutils git nasm
RUN pip install firebase_admin
RUN chmod +x helper

ENTRYPOINT ./helper
