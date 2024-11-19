from pygame.sprite import Sprite
from settings import *
from resources import Resources


class MonsterManager:
    def __init__(self):
        self._monster_sprites = pygame.sprite.Group()  # Sprite group for all monsters

    def add_monster(self, name):
        # Create a new Monster and add to the lists/groups
        # Load configuration based on monster name
        pos = (-100, -100)

        config = MONSTER_CONFIGS.get(name)
        if config is None:
            raise ValueError(f"No configuration found for monster name: {name}")

        Monster(name, pos, self._monster_sprites, config)

    def calc_resource_yield(self):
        mon_yield = Resources()
        for monster in self.monster_sprites:
            mon_yield += monster.gather_resources()

        return mon_yield

    def update(self):
        pass

    @property
    def monster_sprites(self):
        return self._monster_sprites


class Monster(Sprite):
    # FIXME monsters need setters and getters for all propeties
    def __init__(self, name, pos, group, config):
        # Initialize the base Sprite class
        super().__init__(group)

        # Assign monster stats from config
        self.name = name
        self.health = config["health"]
        self.health_cur = self.health
        self.attack = config["attack"]

        # Resources
        self.mana_yield = config["mana_yield"]
        self.essence_yield = config["essence_yield"]
        self.gold_yield = 0

        # Abilities

        # Position and sprite setup
        self.image = config["image"]
        self.rect = self.image.get_frect(topleft=pos)

    def gather_resources(self):
        return Resources(self.mana_yield, self.essence_yield, self.gold_yield)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()  # Remove from all sprite groups if health drops to zero

    def update(self):
        pass



