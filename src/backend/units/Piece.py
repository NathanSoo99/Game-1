from .PieceData import data

class Piece(object):
    def __init__(self, type):
        self.combat_strength = data["combat strength"][type]
        self.movement_range = data["movement range"][type]

    def get_combat_strength(self):
        return self.combat_strength
    
    def get_movement_range(self):
        return self.movement_range