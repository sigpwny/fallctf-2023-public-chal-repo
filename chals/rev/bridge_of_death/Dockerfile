# To build `chal` to current directory, run:
# DOCKER_BUILDKIT=1 docker build . --target release --output type=local,dest=.

FROM ubuntu:20.04 as build

RUN apt-get update && apt-get install -y build-essential

WORKDIR /
COPY bridge.c .
COPY Makefile .

RUN make

FROM scratch as release

COPY --from=build /bridge /bridge
