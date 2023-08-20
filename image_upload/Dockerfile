FROM php:8.2-alpine

RUN apk add --no-cache git python3 python3-pip py3-requests py3-beautifulsoup4

WORKDIR /
COPY . .

RUN chmod +x helper
RUN pip install firebase_admin

ENTRYPOINT helper
