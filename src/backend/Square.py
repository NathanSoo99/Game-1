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
        Remove piece belonging to team and return it
        """
        temp = self.piece
        self.piece = None
        return temp

    
    def change_combat_strength(self, amount, team):
        """
            Adjust team combat strength of square by a specified amount and
            remove piece if opposing combat strength is higher than allied team
            combat strength

            Parameters
                amount (int): numerical amount ()

            Return
                Piece: if opposite team combat strength is higher than allied
                team combat strength return piece otherwise return None
        """
        # Adjust combat strength of corresponding team
        self.combat_strength[team] += amount

        # Get return value
        result = None

        if self.piece is not None:
            team = self.piece.get_team()

            # Check which team has control of square if any
            higher_team = None
            higher_strength = -1
            for key, value in self.combat_strength.items():
                if value > higher_strength:
                    higher_team = key
                    higher_strength = value
                elif value == higher_strength:
                    higher_team = None

            # Remove piece if conditions are met
            if higher_team is not None and team != higher_team:
                result = self.piece
                self.piece = None

        return result

    
    def get_combat_strength(self, team):
        return self.combat_strength[team]