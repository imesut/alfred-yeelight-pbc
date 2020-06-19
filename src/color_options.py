import json, sys
from utils import get_alfred_object
from colors import colors

response_array = []
args = sys.argv

for color in colors:
    response_array.append(get_alfred_object([color, color.capitalize(), "", color, color, "%s.png" % (color)]))

response = {"items": response_array}
print(json.dumps(response))