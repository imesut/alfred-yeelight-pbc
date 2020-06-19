import json, yeelight, sys
from utils import get_alfred_object

ip = "192.168.1.101"
bulb = yeelight.Bulb(ip)
bulb_properties = bulb.get_properties()
current_brightness = bulb_properties["current_brightness"]

response_array = []
item = ["hede", "Title", "subtitle", "arg", "autocomplete", "icon.png"]

# Brightness list
current_brigthness_index = round(int(current_brightness)/10)
#print(current_brigthness_index)
brightness_list = [0,10,20,30,40,50,60,70,80,90,100]
brightness_list = brightness_list[current_brigthness_index:] + brightness_list[:current_brigthness_index]

for option in brightness_list:
    item[0], item[1] = option, "%%%s" % (option)
    item[2]=""
    item[3]=option
    response_array.append(get_alfred_object(item))

response_array[0]["subtitle"] = "Current Brightness"

# print(response_array)

response = {"items": response_array}

print(json.dumps(response))
