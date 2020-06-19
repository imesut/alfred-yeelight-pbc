import json, yeelight, sys
from utils import get_alfred_object, bulb, bulb_properties, current_brightness

current_brigthness_index = round(int(current_brightness)/10)
brightness_list = [0,10,20,30,40,50,60,70,80,90,100]
brightness_list = brightness_list[current_brigthness_index:] + brightness_list[:current_brigthness_index]

response_array = []
for option in brightness_list:
    item = [option, "%%%s" % (option), "", option, "", ""]
    response_array.append(get_alfred_object(item))

response_array[0]["subtitle"] = "Current Brightness"

response = {"items": response_array}
print(json.dumps(response))
