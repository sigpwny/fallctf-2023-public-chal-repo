FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 python3-pip

SHELL ["/bin/bash", "--login", "-i", "-c"]

COPY flag.txt /
RUN chmod 444 /flag.txt

RUN adduser chal

RUN mkdir -p /chal
WORKDIR /chal

COPY requirements.txt ./
RUN pip3 install -r requirements.txt
ADD templates ./templates
COPY main.py templating.py ./

RUN chmod 555 main.py
USER chal

EXPOSE 1337

CMD python3 -m uvicorn --host "0.0.0.0" --port "1337" main:app