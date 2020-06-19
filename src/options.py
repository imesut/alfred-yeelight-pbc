import json, yeelight, sys
from utils import get_alfred_object, bulb

# Properties
bulb_properties = bulb.get_properties()
current_brightness = bulb_properties["current_brightness"]
current_power = bulb_properties["power"]

power = {"on": "off", "off": "on"}
status = power[current_power]

# Result
item = ["toggle_light", "Turn Light " + status.capitalize(), "", status, status, "%s.png" % (status)]

response_array = [ get_alfred_object(item) ]
response = {"items": response_array}
print(json.dumps(response))

#print(yeelight.discover_bulbs())
