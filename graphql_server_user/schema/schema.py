from dataclasses import dataclass
from ariadne import ObjectType, QueryType, snake_case_fallback_resolvers
from ariadne_extensions.federation import FederatedManager, FederatedObjectType

from schema.data_interface import DataStorage

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

"""
Dataclasses, These need to be defined for Boundry Types (A GraphQL type from another server that you are Extending
"""
@dataclass
class User(BoundaryGeneric):
    def __init__(self, **kwargs):
        super().__init__(self.__class__.__name__, kwargs)

"""
Creates the Schema and adds the Federation Declerations to it according to the [https://www.apollographql.com/docs/apollo-server/federation/federation-spec/](Apollo Spec).
"""
class SchemaCreator:

    query = QueryType()
    user = FederatedObjectType("User")

    def __init__(self):
        self.ds = DataStorage()

    def getSchema(self):

        manager = FederatedManager(
            schema_sdl_file='schema/schema.graphql',
            query=self.query,
        )

        @self.query.field("users")
        def resolve_users(*_, **kwargs):
            return self.ds.getUser(**kwargs)

        @self.user.resolve_references
        def resolve_user_references(representations):
            results = []

            for req in representations:
                kwargs = {
                    "id": req.get('id')
                }

                data = self.ds.getUser(**kwargs)[0]
                results.append(User(**data))

            return results

        manager.add_types(self.user)
        manager.add_types(snake_case_fallback_resolvers)

        return manager.get_schema()