import json, yeelight, sys
from utils import get_alfred_object

ip = "192.168.1.101"
#bulb = yeelight.Bulb(os.getenv('bulb_ip', ''))
bulb = yeelight.Bulb(ip)
bulb_properties = bulb.get_properties()
# print(bulb_properties)
current_brightness = bulb_properties["current_brightness"]
current_power = bulb_properties["power"]

power = {"on": "off", "off": "on"}

# print(power[current_power])