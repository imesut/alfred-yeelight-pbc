import yeelight

# item = ["hede", "Title", "subtitle", "arg", "autocomplete", "icon.png"]

ip = "192.168.1.101"
#bulb = yeelight.Bulb(os.getenv('bulb_ip', ''))
bulb = yeelight.Bulb(ip)
bulb_properties = bulb.get_properties()
current_brightness = bulb_properties["current_brightness"]
current_power = bulb_properties["power"]

def get_alfred_object(item_array):
    if len(item_array) == 6:
        return {
            "uid": item_array[0],
            "title": item_array[1],
            "subtitle": item_array[2],
            "arg": item_array[3],
            "autocomplete": item_array[4],
            "icon": {
                "path": item_array[5]
            }
        }
