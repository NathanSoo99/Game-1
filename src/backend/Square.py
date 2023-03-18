from .GameData import game_data

class Square(object):
    def __init__(self):
        """
        Initialize empty square
        """
        super().__init__()

        team_1 = game_data["identifiers"]["team-1"]
        team_2 = game_data["identifiers"]["team-2"]

        self.piece = None

        self.combat_strength = {
            team_1: 0,
            team_2: 0
        }

    def get_pieces(self, team):
        """
        Get piece on this square from team

        Parameters
            team (string): team identifier
        
        Return 
            Piece: requested piece object
        """

        return self.pieces["team"]
    
    def add_piece(self, piece):
        """
        Add piece if there is not already a piece from the same team
        occupying the square

        Parameters
            piece (Piece): piece to be added to square
            team (string): team identifier
        """
        self.piece = piece

    def remove_piece(self, team):
        """
        Remove piece belonging to team
        """
        temp = self.pieces[team]
        self.pieces[team] = None

    
    def change_combat_strength(self, amount, team):
        """
            Adjust team combat strength of square by a specified amount

            Parameters
                amount (int): numerical amount ()
        """
        self.combat_strength[team] += amount
    
    def get_combat_strength(self, team):
        return self.combat_strength[team]