import json, yeelight, sys
from utils import get_alfred_object, bulb

status = sys.argv[-1]

if status == "on":
    bulb.turn_on()
elif status == "off":
    bulb.turn_off()

# response_array = get_alfred_object(["power_uid", "Title", "subtitle", "arg", "autocomplete", "icon.png"])

# response = {"items": response_array}

# print(json.dumps(response))