import json
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './game_data.json')

data = open(filename)
game_data = json.load(data)