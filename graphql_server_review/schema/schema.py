from dataclasses import dataclass

from ariadne import ObjectType, QueryType, snake_case_fallback_resolvers
from ariadne_extensions.federation import FederatedManager, FederatedObjectType

from schema.data_interface import DataStorage

"""
Dataclasses, These need to be defined for Boundry Types (A GraphQL type from another server that you are Extending
"""
@dataclass
class BoundaryGeneric:

    def __init__(self, child_name, kwargs=None):
        self.typename = child_name

        if kwargs:
            self.update_class(kwargs)

        self.get_updated()

    def update_class(self, kwargs):
        for k, v in kwargs.items():
            if not hasattr(self, k):
                setattr(self, k, v)

    def get_updated(self):
        return self

class Photo(BoundaryGeneric):
    def __init__(self, **kwargs):
        super().__init__(self.__class__.__name__, kwargs)

class User(BoundaryGeneric):
    def __init__(self, **kwargs):
        super().__init__(self.__class__.__name__, kwargs)

"""
Creates the Schema and adds the Federation Declerations to it according to the [https://www.apollographql.com/docs/apollo-server/federation/federation-spec/](Apollo Spec).
"""
class SchemaCreator:

    query = QueryType()

    photo = FederatedObjectType("Photo")
    review = FederatedObjectType("Review")
    user = FederatedObjectType("User")

    def __init__(self):
        self.ds = DataStorage()

    def getSchema(self):

        manager = FederatedManager(
            schema_sdl_file='schema/schema.graphql',
            query=self.query,
        )

        @self.query.field("review")
        def resolve_review(*_, **kwargs):
            return self.ds.getReview(**kwargs)

        @self.photo.resolve_reference
        def resolve_photo(representation):
            photo_id = representation.get('id')
            return Photo(id=photo_id)

        @self.photo.field("reviews")
        def resolve_photo_reviews(obj, info):
            kwargs = {
                "photo_id": obj.id
            }
            return self.ds.getReview(**kwargs)

        @self.review.field("reviewer")
        def resolve_reviewer(obj, info):
            user_id = obj["user_id"]
            return User(id=user_id)

        manager.add_types(self.photo, self.review)
        manager.add_types(snake_case_fallback_resolvers)

        return manager.get_schema()