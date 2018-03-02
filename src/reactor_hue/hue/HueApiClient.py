import json
from pathlib import Path

import requests
import os

from reactor_hue.hue.HueLight import HueLight
from reactor_hue.hue.sensors.LightSensor import LightSensor
from reactor_hue.hue.sensors.MotionSensor import MotionSensor
from reactor_hue.hue.sensors.TemperatureSensor import TemperatureSensor

SENSOR_DICT = {
    "ZLLPresence": MotionSensor,
    "ZLLTemperature": TemperatureSensor,
    "ZLLLightLevel": LightSensor
}


class HueApiClient:
    def __init__(self, api_base, device_id, username):
        self.api_base = api_base
        self.device_id = device_id
        self.home = str(Path.home())
        self.username = username
        if username is None:
            if os.path.isfile(self.home + "/.reactor_hue/hue-username.txt"):
                with open(self.home + "/.reactor_hue/hue-username.txt", "r") as username_file:
                    self.username = username_file.read()
            else:
                print("file doesn't exist")

    def _generate_full_base_api(self):
        return self.api_base + "/api/" + self.username

    def _generate_lights_api(self, extra=""):
        return self._generate_full_base_api() + "/lights/" + extra

    def _generate_sensor_api(self, extra=""):
        return self._generate_full_base_api() + "/sensors/" + extra

    def register(self):
        response = requests.post(self.api_base + "/api", data=json.dumps({"devicetype": self.device_id}))
        print(response.text)
        response_dict = response.json()[0]
        if "error" in response_dict:
            return "Error", False
        else:
            if not os.path.isdir(self.home + "/.reactor_hue"):
                os.mkdir(self.home + "/.reactor_hue")
            with open(self.home + "/.reactor_hue/hue-username.txt", "w+") as username_file:
                username_file.write(response_dict["success"]["username"])
                self.username = response_dict["success"]["username"]
            return response_dict["success"]["username"], True

    def get_lights(self):
        response = requests.get(self._generate_full_base_api() + "/lights")
        light_list = list()
        for key, value in response.json().items():
            light_list.append(HueLight(key, value))
        print(json.dumps([ob.__dict__ for ob in light_list]))
        return light_list

    def search_for_lights(self):
        response = requests.post(self._generate_lights_api())
        return response.json()

    def get_light_attributes(self, light_id):
        response = requests.get(self._generate_lights_api(light_id))
        return HueLight(light_id, response.json())

    def rename_light(self, light_id, new_name):
        response = requests.put(self._generate_lights_api(light_id),
                                data=json.dumps({"name": new_name}))
        return response.json()

    def update_light_state(self, light_id, new_state):
        response = requests.put(self._generate_lights_api(light_id + "/state"),
                                data=json.dumps(new_state))
        return response.json()

    def get_sensors(self):
        response = requests.get(self._generate_sensor_api())
        sensor_list = dict()
        for key, value in response.json().items():
            if value['type'] in SENSOR_DICT:
                if value['type'] not in sensor_list:
                    sensor_list[value['type']] = list()
                sensor_list[value['type']].append(SENSOR_DICT[value['type']](key, value))
        print(json.dumps([ob.__dict__ for ob in sensor_list["ZLLPresence"]]))
