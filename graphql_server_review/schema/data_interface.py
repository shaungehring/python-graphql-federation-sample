import objectpath

class DataQuery:

    tree = None

    def __init__(self, json_data):
        self.tree = objectpath.Tree(json_data)

    def queryObjectTree(self, json_query):

        results = list(self.tree.execute(json_query))

        return results

    def getObjectFilterString(self, argument_dictionary: dict):

        filter_string = ""
        i = 1

        if len(argument_dictionary.items()) > 0:
            filter_string = "["

            for k, v in argument_dictionary.items():
                if type(v) == str:
                    v = "'{v}'".format(v=v)

                filter_string = filter_string + "@.{k} is {v}".format(k=k, v=v)

                if i < len(argument_dictionary.items()):
                    filter_string = filter_string + " and "

                i += 1

            filter_string = filter_string + "]"

        return filter_string

class DataStorage:

    data = None
    dq = None

    def __init__(self):
        self.loadData()
        self.dq = DataQuery(json_data=self.data)

    def loadData(self):

        self.data = [
            {
                "id": 10000,
                "user_id": 100,
                "photo_id": 1000,
                "title": "Great Photo",
                "body": "Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, "
            },
            {
                "id": 10001,
                "user_id": 102,
                "photo_id": 1001,
                "title": "Great Photo",
                "body": "Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, "
            },
            {
                "id": 10002,
                "user_id": 101,
                "photo_id": 1002,
                "title": "Great Photo",
                "body": "Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, "
            },
            {
                "id": 10003,
                "user_id": 102,
                "photo_id": 1003,
                "title": "Great Photo",
                "body": "Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, "
            },
            {
                "id": 10004,
                "user_id": 101,
                "photo_id": 1004,
                "title": "Great Photo",
                "body": "Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, "
            },
            {
                "id": 10005,
                "user_id": 100,
                "photo_id": 1005,
                "title": "Great Photo",
                "body": "Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, "
            },

        ]

    def getReview(self, **kwargs):
        filter_string = self.dq.getObjectFilterString(argument_dictionary=kwargs)

        json_query = "$.*{filters}".format(filters=filter_string)

        return self.dq.queryObjectTree(json_query=json_query)
