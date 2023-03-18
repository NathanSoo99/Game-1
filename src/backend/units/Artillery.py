from .Piece import Piece
from .PieceData import data

class Artillery(Piece):
    type = "artillery"

    def __init__(self, team):
        super().__init__(self.type, team)
