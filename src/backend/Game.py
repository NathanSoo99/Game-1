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

        # Generate empty board
        self.board = []
        for y in range(0, 16):
            column = []
            for x in range(0, 16):
                column.append(Square(None, None))

            self.board.append(column)

        # Add pieces and calculate combat strength
        initial_state = game_data["setup"]
    
    def change_strength(self):
        pass    

    def check_move_valid(self):
        pass

    def get_board(self):
        return self.board
    
    def move(self):
        pass

