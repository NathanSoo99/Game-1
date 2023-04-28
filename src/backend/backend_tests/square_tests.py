import pytest

from ..GameData import game_data
from ..Square import Square
from ..units.Infantry import Infantry

team_1 = game_data["identifiers"]["team-1"]
team_2 = game_data["identifiers"]["team-2"]

def test_square_initialize():
    square = Square()
    
    assert square.get_piece() is None
    assert square.remove_piece() is None

    assert square.get_combat_strength(team_1) == 0
    assert square.get_combat_strength(team_2) == 0

    assert square.change_combat_strength(-1, team_1) is None
    assert square.change_combat_strength(-1, team_2) is None
    assert square.change_combat_strength(2, team_1) is None
    assert square.change_combat_strength(2, team_2) is None

    assert square.get_combat_strength(team_1) == 1
    assert square.get_combat_strength(team_2) == 1

def test_square_with_piece():
    piece = Infantry(team_1)
    square = Square()

    square.add_piece(piece)

    assert square.get_piece() == piece
    assert square.remove_piece() == piece
    assert square.get_piece() == None

def test_square_change_combat_strength():
    piece = Infantry(team_1)
    square = Square()

    square.add_piece(piece)
    
    assert square.change_combat_strength(1, team_1) is None
    assert square.get_combat_strength(team_1) == 1
    assert square.get_combat_strength(team_2) == 0
    assert square.get_piece() == piece

    assert square.change_combat_strength(1, team_2) is None
    assert square.get_combat_strength(team_1) == 1
    assert square.get_combat_strength(team_2) == 1
    assert square.get_piece() == piece
    
    assert square.change_combat_strength(1, team_2) == piece
    assert square.get_combat_strength(team_1) == 1
    assert square.get_combat_strength(team_2) == 2
    assert square.get_piece() is None