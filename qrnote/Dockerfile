FROM alpine:latest

WORKDIR /
COPY . .

RUN apk add --no-cache git python3 py3-pip libzbar py3-requests py3-beautifulsoup4
RUN python3 -m pip install --no-cache-dir --upgrade -r requirements.txt
RUN mkdir /app/static/codes

RUN chmod +x helper
RUN pip install firebase_admin

ENTRYPOINT helper
