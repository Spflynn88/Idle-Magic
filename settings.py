from typing import Tuple

import pygame
import os.path
from os import listdir
import random
from utils import *

SCREEN_WIDTH = 1792 # 1280
SCREEN_HEIGHT = 1024 # 800

SPRITE_FOLDER = os.path.join('.', 'sprites')

RESOURCE_GAIN_TIME = 5000 # In ms for timer

# Start Vars
STRT_POP_MAX = 10
STRT_MANA_CAP = 100
STRT_ESS_CAP = 100

# UI Loaction Data


STD_MARGIN_Y = int(SCREEN_HEIGHT * .035)
STD_MARGIN_X = int(SCREEN_WIDTH * .06)

UI_RESOURCE_BAR_POS = (SCREEN_WIDTH // 2, 24) # Resource Bar
UI_MON_ROSTER_POS = (16, 24) # Monster Roster Panel

BUILD_GRID_COLS = 20
BUILD_GRID_ROWS = 20
BUILD_GRID_TILE = 32
BUILD_GRID_START_POS = (350, UI_RESOURCE_BAR_POS[1] + STD_MARGIN_Y + 64) # FIXME - this is a good idea but needs to be where i can get the info

SUMMON_PANE_START_POS = (
    BUILD_GRID_START_POS[0],
    BUILD_GRID_START_POS[1] + (BUILD_GRID_ROWS * BUILD_GRID_TILE) + STD_MARGIN_Y
)


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
