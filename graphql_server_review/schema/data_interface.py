import objectpath

class DataStorage:

    data = None
    tree = None

    def __init__(self):
        self.loadData()

    def loadData(self):

        self.data = [
            {
                "id": 10000,
                "user_id": 103,
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
                "user_id": 103,
                "photo_id": 1002,
                "title": "Great Photo",
                "body": "Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, "
            },
            {
                "id": 10003,
                "user_id": 103,
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
                "user_id": 102,
                "photo_id": 1005,
                "title": "Great Photo",
                "body": "Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, Lorem Ipsum Set Adore, "
            },

        ]

        self.tree = objectpath.Tree(self.data)

    def queryObjectTree(self, json_query):

        results = list(self.tree.execute(json_query))

        return results

    def getReviewById(self, review_id: str):

        json_query = "$.*[@.id is {review_id}]".format(review_id=review_id)

        return self.queryObjectTree(json_query=json_query)

    def getReviewsByPhotoId(self, photo_id: str):

        json_query = "$.*[@.photo_id is {photo_id}]".format(photo_id=photo_id)

        return self.queryObjectTree(json_query=json_query)

    def getReviewsByUserId(self, user_id: str):

        json_query = "$.*[@.user_id is {user_id}]".format(user_id=user_id)

        return self.queryObjectTree(json_query=json_query)