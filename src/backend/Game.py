from .units.Piece import Piece
from .units.General import General
from .units.Infantry import Infantry
from .units.Cavalry import Cavalry
from .units.Artillery import Artillery
from .Square import Square

class Game:
    def __init__(self):
        grid = []
        for x in range(0, 16):
            column = []
            for y in range(0, 16):
                column.append(Square())