FROM node:10

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install
RUN npm install -g nodemon
RUN npm install express --save

COPY . .