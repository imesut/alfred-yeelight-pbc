import json, yeelight, sys
from utils import get_alfred_object, bulb
import colors

color = sys.argv[-1]
color = colors.colors[color]

bulb.set_rgb(color[0], color[1], color[2])