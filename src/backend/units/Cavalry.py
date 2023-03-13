from .Piece import Piece
from .PieceData import data

class Cavalry(Piece):
    type = "cavalry"

    def __init__(self):
        super().__init__(type)