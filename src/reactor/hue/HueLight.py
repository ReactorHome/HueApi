

class HueLight():
    def __init__(self, id, values):
        # self.state = values["state"]
        # self.type = values["type"]
        # self.name = values["name"]
        # self.modelid = values["modelid"]
        # self.swversion = values["swversion"]
        # self.id = id
        self.type = 0
        self.hardware_id = values["uniqueid"]
        self.connected = values["state"]["reachable"]
        self.name = values["name"]
        self.manufacturer = "Philips"
        self.model = values["modelid"]
        self.on = values["state"]["on"]
        self.brightness = values["state"]["bri"] if "bri" in values["state"] else None
        self.supports_color = True if "colormode" in values["state"] else False
        self.color_mode = values["state"]["colormode"] if "colormode" in values["state"] else None
        self.hue = values["state"]["hue"] if "hue" in values["state"] else None
        self.saturation = values["state"]["sat"] if "sat" in values["state"] else None
        self.xy = values["state"]["xy"] if "xy" in values["state"] else None
        self.color_temperature = values["state"]["ct"] if "ct" in values["state"] else None
