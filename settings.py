from typing import Tuple

import pygame
import os.path
from os import listdir
import random

SCREEN_WIDTH = 1792 # 1280
SCREEN_HEIGHT = 1024 # 800

SPRITE_FOLDER = os.path.join('.', 'sprites')

TILE_SIZE = 112

RESOURCE_GAIN_TIME = 1000 # In ms for timer

# Start Vars
STRT_POP_MAX = 10
STRT_MANA_CAP = 100
STRT_ESS_CAP = 100

# UI Loaction Data
# FIXME - I need to figure this out better, maybe base objects of each other
UI_RESOURCE_BAR_POS: tuple[int, int] = (SCREEN_WIDTH // 2, 24) # Resource Bar

UI_MON_ROSTER_POS: tuple[int, int] = (16, 24) # Monster Roster Panel



MON_ICON_SIZE = 128  # They are square so only 1 digit needed
MON_ICON_OFFSET = 16  # Offset inbetween icons on the roster


# Monsters
# Monster configurations
MONSTER_CONFIGS = {
    "Mana_Imp": {"health": 10,
                 "attack": 2,
                 "defense": 1,
                 "type": "arcane",
                 "mana_yield": 5,
                 "essence_yield": 5,
                 "currentXP": 0,
                 "level": 0,
                 "image": "mon_mana_imp",
                 "hp_per_lvl": 1,
                 "attack_per_level": 1,
                 "defense_per_lvl": 1}
}
