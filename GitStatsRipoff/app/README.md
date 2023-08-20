# GitRepoStats

## General Docker Instructions
- build   : `docker build -t <container_image_name> .`
- run     : `docker run -d --name <container_name> <container_image_name>`
- remove  : `docker stop <container_name>; docker rm <container_name>`
- test    : `docker exec -it <container_name> /test/run`


## Instructions to Run

### Inside of a docker container(recommended)
- Ensure the following line is in your Dockerfile
```Dockerfile
ENTRYPOINT ["python", "/app/main.py"]
```
- Build the docker image
```bash
docker build -t <image_name> .
``` 
- Run the docker image in interactive mode `(-it)`
```bash
docker run --name <container_name> -it <image_name>
``` 

### Using a Virtual Environment
It is preferrable to run the code in a docker container as it is easier to setup and run (and good for security reasons). However, if you wish to run the code in a virtual environment, follow the steps below.
- Create a virtual environment
```bash
python -m venv .venv
```
- Activate the virtual environment
```bash
source .venv/bin/activate
```
- Make sure you have `git` and `cloc` installed
A guide to installing `cloc` can be found [here](https://github.com/AlDanial/cloc#install-via-package-manager) and for `git` [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

- Install the dependencies
```bash
pip install -r requirements.txt
```
- Run the code
```bash
python main.py
```

## Instructions for accessing files inside the docker container. 

Sometimes it's more convenient to access the files inside the docker container, modify the files in the container itself and run the code. To do this, follow the steps below.

- Ensure the following line is in your Dockerfile
```Dockerfile
ENTRYPOINT ['tail', '-f', '/dev/null']
```
- Build the docker image
```bash
docker build -t <image_name> .
```
- Run the docker image in detatched mode `(-d)`
```bash
docker run --name <container_name> -d <image_name>
```

- Run bash to access the files inside the container
```bash
docker exec -it <container_name> /bin/bash
```

You can also put your own packages inside the container if you wish to do so(like vim or some other text editor since there is none by default)

