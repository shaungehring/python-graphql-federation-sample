from dataclasses import dataclass

from ariadne import ObjectType, QueryType, snake_case_fallback_resolvers
from ariadne_extensions.federation import FederatedManager, FederatedObjectType

from schema.data_interface import DataStorage

"""
Dataclasses, These need to be defined for Boundry Types (A GraphQL type from another server that you are Extending
"""
@dataclass
class User:
    id: str
    typename: str = "User"

"""
Creates the Schema and adds the Federation Declerations to it according to the [https://www.apollographql.com/docs/apollo-server/federation/federation-spec/](Apollo Spec).
"""
class SchemaCreator:

    def __init__(self):
        self.ds = DataStorage()

    def getSchema(self):

        query = QueryType()

        manager = FederatedManager(
            schema_sdl_file='schema/schema.graphql',
            query=query,
        )

        @query.field("photo")
        def resolve_photo(*_, photo_id=None):
           return self.ds.getPhotoById(photo_id=photo_id)

        user = FederatedObjectType("User")

        @user.resolve_reference
        def resolve_user(representation):
            user_id = representation.get('id')
            return User(id=user_id)

        @user.field("photos")
        def resolve_user_photos(obj, info):
            user_id = obj.id
            return self.ds.getPhotosByUserId(user_id=user_id)

        photo = ObjectType("Photo")

        manager.add_types(user, photo)
        manager.add_types(snake_case_fallback_resolvers)

        return manager.get_schema()