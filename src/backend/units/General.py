from .Piece import Piece

class General(Piece):
    type = "general"

    def __init__(self, team):
        super().__init__(self.type, team)