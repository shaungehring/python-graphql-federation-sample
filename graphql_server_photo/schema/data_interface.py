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
                "id": 1000,
                "user_id": 100,
                "url": "https://upload.wikimedia.org/wikipedia/en/thumb/b/be/Han_Solo_depicted_in_promotional_image_for_Star_Wars_%281977%29.jpg/220px-Han_Solo_depicted_in_promotional_image_for_Star_Wars_%281977%29.jpg"
            },
            {
                "id": 1001,
                "user_id": 100,
                "url": "https://pbs.twimg.com/media/BlrdTeMIQAAN1rv.jpg"
            },
            {
                "id": 1002,
                "user_id": 101,
                "url": "https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/Princess_Leia%27s_characteristic_hairstyle.jpg/220px-Princess_Leia%27s_characteristic_hairstyle.jpg"
            },
            {
                "id": 1003,
                "user_id": 101,
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Star_Wars_and_the_Power_of_Costume_July_2018_24_%28Princess_Leia%27s_Boushh_disguise_and_thermal_detonator_from_Episode_VI%29.jpg/220px-Star_Wars_and_the_Power_of_Costume_July_2018_24_%28Princess_Leia%27s_Boushh_disguise_and_thermal_detonator_from_Episode_VI%29.jpg"
            },
            {
                "id": 1004,
                "user_id": 102,
                "url": "https://media.gq.com/photos/56da0101062ab67b27facbd2/16:9/w_2560%2Cc_limit/luke-skywalker-gay-.jpg"
            },
            {
                "id": 1005,
                "user_id": 102,
                "url": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/luke-anakin-star-war-1565875142.jpg?crop=0.495xw:0.990xh;0,0&resize=480:*"
            },
        ]

    def getPhoto(self, **kwargs):
        filter_string = self.dq.getObjectFilterString(argument_dictionary=kwargs)

        json_query = "$.*{filters}".format(filters=filter_string)

        return self.dq.queryObjectTree(json_query=json_query)