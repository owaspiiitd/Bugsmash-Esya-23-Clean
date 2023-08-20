# Golden Ticket

Integer overflow

Should pass iff run.sh prints only `pass` on all lines.

Compilation errors are also handled at runtime.

## Usage

build        : `docker build -t <container_image_name> .`
run and test : `docker run --name <container_name> <container_image_name>`
remove       : `docker stop <container_name>; docker rm <container_name>`
test         : `docker exec -it <container_name> /test/run`

**NOTE**: NO DETACHED MODE, testing and running is integrated
