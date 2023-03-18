import json
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './piece_data.json')

piece_file = open(filename)
data = json.load(piece_file)