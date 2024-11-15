# PopulationManager ResourceManager
import pygame
from settings import *

# PopulationManager keeps track of the population numbers and gives permission to summon
# List of individual monsters and their actions will be managed by the MonsterManager


class Resources:
    def __init__(self, mana=0, essence=0, veil_pearls=0, gems_raw=0):
        self.mana = mana
        self.essence = essence
        self.vpearls = veil_pearls
        self.gems_raw = gems_raw
        self.gems_refined = {
            "arcane": 0,
            "void": 0,
            "flame": 0,
            "aqua": 0,
            "wild": 0,
            "stone": 0
        }

    def __repr__(self):
        return f"Resources(mana={self.mana}, essence={self.essence}, vpearls={self.vpearls})"

    def __add__(self, other):
        if not isinstance(other, Resources):
            return NotImplemented

        return Resources(
            self.mana + other.mana,
            self.essence + other.essence,
            self.vpearls + other.vpearls

        )


class PopulationManager:
    def __init__(self):
        self._pop_max = STRT_POP_MAX
        self._pop_cur = 0

    @property
    def pop_cur(self):
        return self._pop_cur

    @pop_cur.setter
    def pop_cur(self, value):
        self._pop_cur = min(value, self._pop_max)  # Ensure pop doesn't exceed max

    @property
    def pop_max(self):
        return self._pop_max

    @pop_max.setter
    def pop_max(self, value):
        if value >= 0:
            self._pop_max = value

    def can_add_monster(self):
        return self._pop_cur < self._pop_max

    def update(self):
        pass


class ResourceManager:
    def __init__(self):
        # Initialize resources with defaults
        self.resources = Resources(5, 5, 5)
        self.mana_max = 100
        self.essence_max = 100
        self.gold_max = 100

    def __repr__(self):
        return (f"ResourceManager(resources={self.resources}, mana_max={self.mana_max}, essence_max={self.essence_max}, "
                f"gold_max={self.gold_max})")

    @property
    def mana(self):
        return self.resources.mana

    @mana.setter
    def mana(self, value):
        # Ensure mana is within allowed bounds
        self.resources.mana = max(0, min(value, self.mana_max))

    @property
    def essence(self):
        return self.resources.essence

    @essence.setter
    def essence(self, value):
        # Ensure essence is within allowed bounds
        self.resources.essence = max(0, min(value, self.essence_max))

    @property
    def gold(self):
        return self.resources.gold

    @gold.setter
    def gold(self, value):
        # Ensure gold is within allowed bounds
        self.resources.gold = max(0, min(value, self.gold_max))

    @property
    def get_resources(self):
        return self.resources

    def update(self):
        # Placeholder for future update logic
        pass

    def add_resources(self, new_resources):
        # Add new resources while ensuring they do not exceed maximums
        self.mana = self.resources.mana + new_resources.mana
        self.essence = self.resources.essence + new_resources.essence
        self.gold = self.resources.gold + new_resources.gold

