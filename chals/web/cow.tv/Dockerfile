FROM ubuntu:22.04
RUN apt-get update && apt-get install -y socat python3 python3-pip cowsay curl

SHELL ["/bin/bash", "--login", "-i", "-c"]

RUN curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash 
RUN source ~/.bashrc
RUN nvm install --lts

COPY flag.txt /
RUN chmod 444 /flag.txt

RUN adduser chal

RUN mkdir -p /chal
WORKDIR /chal

COPY package.json package-lock.json postcss.config.js svelte.config.js tailwind.config.js vite.config.js requirements.txt ./
ADD src ./src
ADD static ./static
COPY chal.py ./
RUN pip3 install -r requirements.txt
RUN npm install
RUN npm run build


RUN chmod 555 chal.py
USER chal

EXPOSE 1337

CMD python3 chal.py