from .Piece import Piece

class Infantry(Piece):
    type = "infantry"

    def __init__(self, team):
        super().__init__(self.type, team)