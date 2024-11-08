import pygame
from pygame.sprite import Sprite
from settings import MONSTER_CONFIGS


class MonsterManager:
    def __init__(self):
        self.monster_sprites = pygame.sprite.Group()  # Sprite group for all monsters

    def add_monster(self, name, pos):
        # Create a new Monster and add to the lists/groups
        # Load configuration based on monster name
        config = MONSTER_CONFIGS.get(name)
        if config is None:
            raise ValueError(f"No configuration found for monster name: {name}")

        Monster(name, pos, self.monster_sprites, config)

    def calc_resource_yield(self):
        _mana_yield = 0
        _essence_yield = 0
        _gold_yield = 0
        for monster in self.monster_sprites:
            mon_yield = monster.gather_resources()
            _mana_yield += mon_yield["mana_yield"]
            _essence_yield += mon_yield["essence_yield"]

        return _mana_yield, _essence_yield, _gold_yield

            # FIXME monsters need setters and getters for all propeties

    def update(self):
        pass

    def render(self, display_surface):
        # Draw all sprites in the monster group to the screen
        self.monster_sprites.draw(display_surface)


class Monster(Sprite):
    def __init__(self, name, pos, group, config):
        # Initialize the base Sprite class
        super().__init__(group)

        # Assign monster stats from config
        self.name = name
        self.health = config["health"]
        self.attack = config["attack"]
        self.mana_yield = config["mana_yield"]
        self.essence_yield = config["essence_yield"]

        # Position and sprite setup
        self.image = config["image"]
        self.rect = self.image.get_rect(topleft=pos)

    def gather_resources(self):
        return {"mana_yield": self.mana_yield, "essence_yield": self.essence_yield}

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()  # Remove from all sprite groups if health drops to zero

    def update(self):
        pass



