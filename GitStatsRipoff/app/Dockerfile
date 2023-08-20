FROM python:slim-bullseye

# Install git and do basic config
RUN apt-get update && apt-get install -y git
RUN apt-get install -y cloc
RUN git config --global user.email "default@123.com"
RUN git config --global user.name "default"

# Install GitPython version 3.1.20
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# # For normal use
# ENTRYPOINT ["python", "main.py"]

# For quick edits
ENTRYPOINT ["tail", "-f", "/dev/null"]
