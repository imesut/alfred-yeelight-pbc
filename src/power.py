import json, yeelight, sys
from utils import get_alfred_object

status = sys.argv[-1]

ip = "192.168.1.101"
#bulb = yeelight.Bulb(os.getenv('bulb_ip', ''))
bulb = yeelight.Bulb(ip)

if status == "on":
    bulb.turn_on()
elif status == "off":
    bulb.turn_off()
elif status == "aaa":
    print("hw")
    bulb.toggle()

response_array = get_alfred_object(["power_uid", "Title", "subtitle", "arg", "autocomplete", "icon.png"])

response = {"items": response_array}

print(json.dumps(response))