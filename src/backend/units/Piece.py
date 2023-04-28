from .PieceData import data

class Piece(object):
    def __init__(self, type, team):
        self.combat_strength = data["combat strength"][type]
        self.movement_range = data["movement range"][type]
        self.attack_range = data["attack range"][type]
        self.team = team

    def get_combat_strength(self):
        return self.combat_strength
    
    def get_movement_range(self):
        return self.movement_range
    
    def get_attack_range(self):
        return self.attack_range
    
    def get_team(self):
        return self.team