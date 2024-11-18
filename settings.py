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


UI_SIDE_PANEL_W = SCREEN_WIDTH * .15
UI_SIDE_PANEL_H = SCREEN_HEIGHT

UI_RESOURCE_BAR_POS = (UI_SIDE_PANEL_W, SCREEN_HEIGHT - 50) # Resource Bar


BUILD_GRID_COLS = 40
BUILD_GRID_ROWS = 25
BUILD_GRID_TILE = 32
BUILD_GRID_START_POS = (270 + 100, 100) # FIXME All of the ui is getting redone



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
