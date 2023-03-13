from .Piece import Piece

class Infantry(Piece):
    type = "infantry"

    def __init__(self):
        super().__init__(type)