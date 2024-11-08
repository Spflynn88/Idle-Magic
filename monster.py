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
        self.resource_type = config["resource_type"]
        self.resource_yield = config["resource_yield"]

        # Position and sprite setup
        self.image = config["image"]
        self.rect = self.image.get_rect(topleft=pos)

    def gather_resources(self):
        return {self.resource_type: self.resource_yield}

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()  # Remove from all sprite groups if health drops to zero

    def update(self):
        pass



