import json

class World:

    _instance = None

    def __new__(cls, *args, **kwargs):

        if not cls._instance:

            cls._instance = super(World, cls).__new__(cls, *args, **kwargs)

        return cls._instance

    def load(self):

        with open('world.json') as json_data:
            self.env = json.load(json_data)
            json_data.close()
            print(self.env)

    def get(self):

        return self.env

