
class LightSensor:
    def __init__(self, hue_id, values):
        self.state = values["state"]
        self.name = values["name"]
        self.type = values["type"]
        self.modelid = values["modelid"]
        self.manufacturername = values["manufacturername"]
        # self.productid = values["productid"]
        self.uniqueid = values["uniqueid"]
        self.swversion = values["swversion"]
        self.config = values["config"]
        self.hue_id = hue_id
