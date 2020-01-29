FROM node:13.7

WORKDIR /code

RUN npm install @apollo/gateway apollo-server graphql

COPY . .

CMD ["node", "gateway.js"]