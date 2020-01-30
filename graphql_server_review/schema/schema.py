from dataclasses import dataclass

from ariadne import ObjectType, QueryType, snake_case_fallback_resolvers
from ariadne_extensions.federation import FederatedManager, FederatedObjectType

from schema.data_interface import DataStorage

"""
Dataclasses, These need to be defined for Boundry Types (A GraphQL type from another server that you are Extending
"""
@dataclass
class Photo:
    id: str
    typename: str = "Photo"

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

        @query.field("review")
        def resolve_review(*_, **kwargs):
           return self.ds.getReview(**kwargs)

        photo = FederatedObjectType("Photo")

        @photo.resolve_reference
        def resolve_photo(representation):
            photo_id = representation.get('id')
            return Photo(id=photo_id)

        @photo.field("reviews")
        def resolve_photo_reviews(obj, info):
            kwargs = {
                "photo_id": obj.id
            }

            return self.ds.getReview(**kwargs)

        review = ObjectType("Review")

        manager.add_types(photo, review)
        manager.add_types(snake_case_fallback_resolvers)

        return manager.get_schema()