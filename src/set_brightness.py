import yeelight, sys
from utils import bulb

args = sys.argv

brightness = int(args[-1])
bulb.set_brightness(brightness)
