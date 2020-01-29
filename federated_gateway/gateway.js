const { ApolloServer } = require('apollo-server');
const { ApolloGateway } = require("@apollo/gateway");

const gateway = new ApolloGateway({
  serviceList: [
    { name: 'user', url: 'http://graphql_server_user:8300' },
    { name: 'photo', url: 'http://graphql_server_photo:8301' },
    { name: 'review', url: 'http://graphql_server_review:8302' },
  ],
});

const server = new ApolloServer({
  gateway,
  subscriptions: false,
});

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});