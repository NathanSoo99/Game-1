from .Piece import Piece

class General(Piece):
    type = "general"

    def __init__(self):
        super().__init__(type)