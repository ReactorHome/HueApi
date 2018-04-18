

class HueLight:
    def __init__(self, internal_id, values):
        self.type = 0
        self.internal_id = internal_id
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

    def __hash__(self):
        return hash(self.hardware_id) ^ hash(self.connected) ^ hash(self.on) ^ \
               hash((self.hardware_id, self.connected, self.hardware_id))

    def __eq__(self, other):
        return (self.hardware_id, self.connected, self.on) == \
               (other.hardware_id, other.connected, other.on)
