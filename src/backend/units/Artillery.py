from .Piece import Piece
from .PieceData import data

class Artillery(Piece):
    type = "artillery"

    def __init__(self):
        super().__init__(self.type)
