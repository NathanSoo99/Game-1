import os
import json

import pytest

from ..Infantry import Infantry
from ..Cavalry import Cavalry
from ..Artillery import Artillery
from ..General import General

# Get piece data
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../piece_data.json')

piece_file = open(filename)
data = json.load(piece_file)

def test_infantry():
    infantry = Infantry("1")

    assert infantry.get_combat_strength() == data["combat strength"]["infantry"]
    assert infantry.get_movement_range() == data["movement range"]["infantry"]
    assert infantry.get_attack_range() == data["attack range"]["infantry"]
    assert infantry.get_team() == "1"

def test_cavalry():
    cavalry = Cavalry("1")

    assert cavalry.get_combat_strength() == data["combat strength"]["cavalry"]
    assert cavalry.get_movement_range() == data["movement range"]["cavalry"]
    assert cavalry.get_attack_range() == data["attack range"]["cavalry"]
    assert cavalry.get_team() == "1"

def test_artillery():
    artillery = Artillery("1")

    assert artillery.get_combat_strength() == data["combat strength"]["artillery"]
    assert artillery.get_movement_range() == data["movement range"]["artillery"]
    assert artillery.get_attack_range() == data["attack range"]["artillery"]
    assert artillery.get_team() == "1"

def test_general():
    general = General("1")

    assert general.get_combat_strength() == data["combat strength"]["general"]
    assert general.get_movement_range() == data["movement range"]["general"]
    assert general.get_attack_range() == data["attack range"]["general"]
    assert general.get_team() == "1"