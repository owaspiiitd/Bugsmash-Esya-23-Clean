FROM python:3.10-slim-buster

# Install git and do basic config
RUN apt-get update && apt-get install -y git
RUN apt-get install -y cloc
RUN git config --global user.email "default@123.com"
RUN git config --global user.name "default"

# Install GitPython version 3.1.20
WORKDIR /

COPY . .

RUN pip install -r /app/requirements.txt

RUN chmod +x /test/run /test/test1 /test/test2 /test/test3 /test/test4

ENTRYPOINT [ "/test/run" ]
