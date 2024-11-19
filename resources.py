# PopulationManager ResourceManager
import pygame
from settings import *

# PopulationManager keeps track of the population numbers and gives permission to summon
# List of individual monsters and their actions will be managed by the MonsterManager

# Mana is excluded from resources as it won't but used for building and just for the idle portion


class Resources:
    def __init__(self, t_essence=0, t_veil_pearls=0, t_gems_raw=0, t_gems_refined=None):
        self.essence = t_essence
        self.vpearls = t_veil_pearls
        self.gems_raw = t_gems_raw

        if t_gems_refined:
            self.gems_refined = t_gems_refined.copy()
        else:
            self.gems_refined = {
                "void": 0,
                "wild": 0,
                "flame": 0,
                "stone": 0,
                "aqua": 0
            }

    def __repr__(self): # FIXME
        #return f"essence={self.essence}, vpearls={self.vpearls}"
        pass

    def __add__(self, t_other):  # FIXME
        if not isinstance(t_other, Resources):
            return NotImplemented

        _gems_refined = self.gems_refined.copy()
        for gem, value in t_other.gems_refined:
            _gems_refined["gem"] += value

        new_resource = Resources(
            self.essence + t_other.essence,
            self.vpearls + t_other.vpearls,
            self.gems_raw + t_other.gems_raw,
            _gems_refined
        )

        return new_resource







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


class ResourceManager:  # FIXME
    def __init__(self):
      pass
