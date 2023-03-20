from .units.Piece import Piece
from .units.General import General
from .units.Infantry import Infantry
from .units.Cavalry import Cavalry
from .units.Artillery import Artillery
from .Square import Square
from .GameData import game_data

class Game(object):
    def __init__(self):
        """ 
        Initialize the initial game conditions
        """
        super().__init__()

        # Generate empty board
        self.board = []
        for y in range(0, 16):
            column = []
            for x in range(0, 16):
                column.append(Square())

            self.board.append(column)

        # Add pieces and calculate combat strength
        initial_state = game_data["setup"]
        self.board_size = len(game_data["setup"])
        self.current_player_turn = game_data["identifiers"]["team-1"]

        y = 0
        for row in initial_state:
            x = 0
            for col in row:
                if col != "n":
                    identifier, team = list(col)
                    new_piece = None
                    if identifier == "I":
                        new_piece = Infantry(team)
                    elif identifier == "C":
                        new_piece = Cavalry(team)
                    elif identifier == "A":
                        new_piece = Artillery(team)
                    elif identifier == "G":
                        new_piece = General(team)
                    self.board[y][x].add_piece(new_piece)
                    self.board_update_piece_introduced(y, x, new_piece)
                x += 1
            y += 1

        self.print_combat_strength(game_data["identifiers"]["team-1"])

    def board_update_piece_removed(self, y, x, piece):
        if piece is None:
            return
        attack_range = piece.get_attack_range()
        combat_strength = piece.get_combat_strength()
        team = piece.get_team()

        for dy in range(0, attack_range + 1):
            for dx in range(0, attack_range + 1):
                if (dy ** 2 + dx ** 2) <= attack_range **2:
                    if y+dy < self.board_size:
                        if x+dx < self.board_size:
                            removed_piece = self.board[y+dy][x+dx].change_combat_strength(-combat_strength, team)
                            if removed_piece is not None: self.board_update_remove_piece(y+dy, x+dx, removed_piece)
                        if x-dx >= 0 and dx != 0:
                            removed_piece = self.board[y+dy][x-dx].change_combat_strength(-combat_strength, team)
                            if removed_piece is not None: self.board_update_remove_piece(y+dy, x-dx, removed_piece)
                    if y-dy >= 0 and dy != 0:
                        if x+dx < self.board_size:
                            removed_piece = self.board[y-dy][x+dx].change_combat_strength(-combat_strength, team)
                            if removed_piece is not None: self.board_update_remove_piece(y-dy, x+dx, removed_piece)
                        if x-dx >= 0 and dx != 0:
                            removed_piece = self.board[y-dy][x-dx].change_combat_strength(-combat_strength, team)
                            if removed_piece is not None: self.board_update_remove_piece(y-dy, x-dx, removed_piece)

         

    def board_update_piece_introduced(self, y, x, piece):
        """
        Update the board state after a piece has been added to a square

        Parameters
            y (int): y coordinate of the square
            x (int): x coordinate of the square
            piece (Piece):
        """
        # Just in case
        if piece is None:
            return
        
        # Necessary parameters
        attack_range = piece.get_attack_range()
        combat_strength = piece.get_combat_strength()
        team = piece.get_team()

        # Update all squares in range of piece
        for dy in range(0, attack_range + 1):
            for dx in range(0, attack_range + 1):
                if (dy ** 2) + (dx ** 2) <= attack_range ** 2:
                    if y+dy < self.board_size:
                        if x+dx < self.board_size:
                            removed_piece = self.board[y+dy][x+dx].change_combat_strength(combat_strength, team)
                            if removed_piece is not None: self.board_update_remove_piece(y+dy, x+dx, removed_piece)
                        if x-dx >= 0 and dx != 0:
                            removed_piece = self.board[y+dy][x-dx].change_combat_strength(combat_strength, team)
                            if removed_piece is not None: self.board_update_remove_piece(y+dy, x-dx, removed_piece)
                    if y-dy >= 0 and dy != 0:
                        if x+dx < self.board_size:
                            removed_piece = self.board[y-dy][x+dx].change_combat_strength(combat_strength, team)
                            if removed_piece is not None: self.board_update_remove_piece(y-dy, x+dx, removed_piece)
                        if x-dx >= 0 and dx != 0:
                            removed_piece = self.board[y-dy][x-dx].change_combat_strength(combat_strength, team)
                            if removed_piece is not None: self.board_update_remove_piece(y-dy, x-dx, removed_piece)


    def print_combat_strength(self, team):
        for row in self.board[::-1]:
            for col in row:
                print(col.get_combat_strength(team), end=" ")
            print()

    def submit_move(self, original_y, original_x, destination_y, destination_x):
        """
        Submit Move

        Parameters
            - original_x (integer): Moved piece's original x coordinate
            - original_y (integer): Moved piece's original y coordinate
            - destination_x (integer): Destination square x coordinate
            - destination_y (integer): Destination square y coordinate
        
        Return
        """
        pass

    def check_move_valid(self, original_y, original_x, destination_y, destination_x):
        """
        Check to see if the move is valid by the following conditions:
            - There is a piece belonging to the current player on the original square
            - Destination square is not already occupied
            - Move is within the piece's movement range

        Parameters
            - original_x (integer): Moved piece's original x coordinate
            - original_y (integer): Moved piece's original y coordinate
            - destination_x (integer): Destination square x coordinate
            - destination_y (integer): Destination square y coordinate

        Return
            - boolean: If the move is valid
        """
        moving_piece = self.board[original_y][original_x].get_piece()
        occupying_piece = self.board[destination_y][destination_x].get_piece()

        if moving_piece is None or moving_piece.get_team() != self.current_player_turn: return False
        if occupying_piece is not None: return False

        movement_range = moving_piece.get_movement_range()

        if (destination_y-original_y) ** 2 + (destination_x-original_x) ** 2 > movement_range ** 2: return False
        return True

