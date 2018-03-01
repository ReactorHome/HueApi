

class HueLight():
    def __init__(self, id, values):
        self.state = values["state"]
        self.type = values["type"]
        self.name = values["name"]
        self.modelid = values["modelid"]
        self.swversion = values["swversion"]
        self.id = id
