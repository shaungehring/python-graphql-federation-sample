# Python GraphQL Federation Sample
This is an example of using GraphQL federation with python. This includes multiple python graphql servers and a federated gateway.

## GraphQL Servers

Each server is made up of a default set of components

- app.py - This is a generic Flask based application file to serve the GraphQL service. This does not need to be modified outside of the Flask Port.
- schema/schema.graphql - This is the standard schema file where you define and document your service.
- schema/schema.py - This is the Class that you will use most. This allows you to create your resolvers and return the final schema to the Flask App
- schema/data_interface.py - This is just me stubbing out a data service so you can test this. You would create your own access to a DB or you could have this access a REST Api if you want.

### Server A (User)
All data asociated with the User
User - [http://localhost:8300]()
### Server B (Photo)
All data asociated with the Photo
Photo - [http://localhost:8301]()
### Server C (Review)
All data asociated with the Review
Review - [http://localhost:8302]()
## Federated Gateway
Gateway - [http://localhost:4000]()

## Docker Compose
To run this demo

```bash
docker-compose up --build
```

The Query Browser will run at [http://localhost:4000]() this is where you can test queries.

The config will also allow you yo use the individual GraphQL servers.

- User - [http://localhost:8300]()
- Photo - [http://localhost:8301]()
- Review - [http://localhost:8302]()

## Sample Queries

This will connect all of the GraphQL Schemas with one query.
```graphql
query {
  users(first_name:"Han"){
    id
    first_name
    last_name
    photos{
      id
      url
      reviews{
        id
        title
        body
      }
    }
  }
}
```

```json
{
  "data": {
    "users": [
      {
        "id": "100",
        "first_name": "Han",
        "last_name": "Solo",
        "photos": [
          {
            "id": "1000",
            "url": "https://upload.wikimedia.org/wikipedia/en/thumb/b/be/Han_Solo_depicted_in_promotional_image_for_Star_Wars_%281977%29.jpg/220px-Han_Solo_depicted_in_promotional_image_for_Star_Wars_%281977%29.jpg",
            "reviews": [
              {
                "id": "10000",
                "title": "Great Photo",
                "body": "Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, "
              }
            ]
          },
          {
            "id": "1001",
            "url": "https://pbs.twimg.com/media/BlrdTeMIQAAN1rv.jpg",
            "reviews": [
              {
                "id": "10001",
                "title": "Great Photo",
                "body": "Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, "
              }
            ]
          }
        ]
      }
    ]
  }
}
```