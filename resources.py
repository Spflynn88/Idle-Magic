# PopulationManager ResourceManager
import pygame
from settings import *

# PopulationManager keeps track of the population numbers and gives permission to summon
# List of individual monsters and their actions will be managed by the MonsterManager
class Resources:
    def __init__(self, mana=0, essence=0, gold=0):
        self.mana = mana
        self.essence = essence
        self.gold = gold

    def __repr__(self):
        return f"Resources(mana={self.mana}, essence={self.essence}, gold={self.gold})"

    def __add__(self, other):
        if not isinstance(other, Resources):
            return NotImplemented

        return Resources(
            self.mana + other.mana,
            self.essence + other.essence,
            self.gold + other.gold

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
        self._mana = 0
        self._mana_max = 100
        self._essence = 0
        self._essence_max = 100

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana = min(value, self._mana_max)  # Ensure mana doesn't exceed max

    @property
    def essence(self):
        return self._essence

    @essence.setter
    def essence(self, value):
        self._essence = min(value, self._essence_max)  # Ensure essence doesn't exceed max

    @property
    def mana_max(self):
        return self._mana_max

    @mana_max.setter
    def mana_max(self, value):
        if value >= 0:
            self._mana_max = value

    @property
    def essence_max(self):
        return self._essence_max

    @essence_max.setter
    def essence_max(self, value):
        if value >= 0:
            self._essence_max = value

    def update(self, t_value):
        # This takes in a tuple for now that is all of the resources listed in order: Mana, Essence, Gold
        self._mana += t_value[0]
        self._essence += t_value[1]

        #return self._mana, self._essence, 0 # ) is for gold yeild, not yet decided on

