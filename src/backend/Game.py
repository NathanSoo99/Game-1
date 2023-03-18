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

    def board_update_piece_removed(self):
        pass

    def board_update_piece_introduced(self, y, x, piece):
        if piece is None:
            return
        attack_range = piece.get_attack_range()
        combat_strength = piece.get_combat_strength()
        team = piece.get_team()
        board_size = len(self.board)
        for dy in range(0, attack_range + 1):
            for dx in range(0, attack_range + 1):
                if (dy ** 2) + (dx ** 2) <= attack_range ** 2:
                    if y+dy < board_size:
                        if x+dx < board_size:
                            self.board[y+dy][x+dx].change_combat_strength(combat_strength, team)
                        if x-dx >= 0 and dx != 0:
                            self.board[y+dy][x-dx].change_combat_strength(combat_strength, team)
                    if y-dy >= 0 and dy != 0:
                        if x+dx < board_size:
                            self.board[y-dy][x+dx].change_combat_strength(combat_strength, team)
                        if x-dx >= 0 and dx != 0:
                            self.board[y-dy][x-dx].change_combat_strength(combat_strength, team)


    def print_combat_strength(self, team):
        for row in self.board[::-1]:
            for col in row:
                print(col.get_combat_strength(team), end=" ")
            print()

    def submit_move(self):
        pass

    def check_move_valid(self):
        pass

    def change_strength(self):
        pass    

    def check_move_valid(self):
        pass

    def get_board(self):
        return self.board
    
    def move(self):
        pass

