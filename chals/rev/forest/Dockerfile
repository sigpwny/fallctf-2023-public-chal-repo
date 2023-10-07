# To build `chal` to current directory, run:
# DOCKER_BUILDKIT=1 docker build . --target release --output type=local,dest=.

FROM --platform=linux/amd64 ubuntu:20.04 as build

RUN apt-get update && apt-get install -y build-essential

WORKDIR /
COPY main.c .
COPY Makefile .

RUN make

FROM scratch as release

COPY --from=build /main /main
