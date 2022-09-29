

FROM node:6-alpine

WORKDIR /usr/src/app

EXPOSE 3000

COPY package.json package.json

RUN npm install && npm cache clean --force

COPY . .
#copy everything from current directory on host to current working directory in image

CMD [ "/sbin/tini", "--", "node", "./bin/www." ]