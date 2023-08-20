# BugSmash Challenge Template

## Challenge Structure
```
bugsmash_template/          # parent directory, this is the maine challenge name
├── Dockerfile*             # this is for setting up the container for the project
├── app*                    # directory containing project files
│   ├── main.py
│   ├── README.md           # project documentation
│   └── ...
│       └── ...
├── test*                   # directory containing test files (contents will be redacted for participants)
│   ├── run*                # shell script that handles execution of tests
│   ├── test1.py            # testing program
│   ├── test2.py
│   └── ...
│       └── ...
└── README.md*              # challenge documentation (for organizers)
```
`NOTE`: files or directories with a `*` must have the same name and position in the challenge directory.

## Dockerfile Structure
```
FROM alpine:latest                          # base container, change this as per requirements

RUN apk add --no-cache python3 py3-pip      # add dependencies required by the project
RUN pip install flask requests

WORKDIR /app                                # create a directory inside container for project files
COPY app/ .                                 # add project files to the container

WORKDIR /test                               # create a directory inside container for test files
COPY test/ .                                # add test files to the container

ENTRYPOINT flask --app /app/main run        # run the project at container startup
```

## Test Structure
- The `run` script handles the execution of all the tests for the project.
- The script can run the tests on its own or it may run other programs in `/test`.
- Every test should only output `pass` or `fail` on a new line. (refer to the output of `run` in this template)

## Usage

build   : `docker build -t <container_image_name> .`
run     : `docker run -d --name <container_name> <container_image_name>`
remove  : `docker stop <container_name>; docker rm <container_name>`
test    : `docker exec -it <container_name> /test/run`
