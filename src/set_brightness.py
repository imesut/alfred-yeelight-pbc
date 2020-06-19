import yeelight, sys

ip = "192.168.1.101"
bulb = yeelight.Bulb(ip)
response_array = []

args = sys.argv

if len(args) > 1:
    brightness = int(args[-1])
    bulb.set_brightness(brightness)