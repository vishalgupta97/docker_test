FROM ubuntu:16.04
FROM node:carbon

RUN apt-get update && \
    apt-get install -y build-essential libssl-dev && \
    apt-get install -y curl git g++ sudo

# RUN useradd -m sunbird && echo "sunbird:sunbird" | chpasswd && adduser sunbird sudo

RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /home/sunbird

COPY sunbird-portal sunbird-portal/
COPY environmentVariablesHelper.js sunbird-portal/src/app/helpers

RUN npm install -g bower
RUN npm install -g gulp-cli

WORKDIR sunbird-portal/src/
RUN npm install

RUN bower cache clean --allow-root

RUN bower install --allow-root

WORKDIR app/

EXPOSE 3000

#ENTRYPOINT ["/bin/bash"]

ENTRYPOINT ["node", "server.js"]
