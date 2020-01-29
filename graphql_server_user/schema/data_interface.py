import objectpath

class DataStorage:

    data = None
    tree = None

    def __init__(self):
        self.loadData()

    def loadData(self):

        self.data = [
            {
                "id": 100,
                "first_name": "Han",
                "last_name": "Solo"
            },
            {
                "id": 101,
                "first_name": "Leia",
                "last_name": "Organa"
            },
            {
                "id": 102,
                "first_name": "Luke",
                "last_name": "Skywalker"
            }
        ]

        self.tree = objectpath.Tree(self.data)

    def queryObjectTree(self, json_query):

        results = list(self.tree.execute(json_query))

        return results

    def getUserById(self, user_id: str):

        json_query = "$.*[@.id is {user_id}]".format(user_id=user_id)

        return self.queryObjectTree(json_query=json_query)

    def getUserByName(self, first_name: str = None, last_name: str = None):

        if first_name and last_name:
            json_query = "$.*[@.first_name is {first_name} and @.last_name is {last_name}]".format(first_name=first_name, last_name=last_name)
        else:
            json_query = "$.*[@.first_name is {first_name} or @.last_name is {last_name}]".format(first_name=first_name, last_name=last_name)

        return self.queryObjectTree(json_query=json_query)