FROM node:18-alpine

COPY pwnydex/ /app/

WORKDIR /app

RUN npm ci

RUN npm run build

CMD ["npm", "run", "start"]