import json, yeelight, sys
from utils import get_alfred_object
import colors


ip = "192.168.1.101"
bulb = yeelight.Bulb(ip)

color = sys.argv[-1]
color = colors.colors[color]

bulb.set_rgb(color[0], color[1], color[2])