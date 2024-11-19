from settings import *
from utils import *
from sys import exit
from building import *

from resources import ResourceManager, PopulationManager, Resources
from monster import MonsterManager
from ui import UIManager
#from spells import SpellManager


# Initialize Pygame
pygame.init()
pygame.mixer.init()


class Game:
    def __init__(self):
        # Set up the game window
        self.display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Idle Magic')
        self.clock = pygame.time.Clock()
        self.dt = 0

        # Vars
        # FIXME - Game doesn't hold the resources the manager does
        # DEL self.resources = Resources() # This is where Game keeps track of the total resources
        self.resource_income = Resources() # This is the resources that are going to be added on update

        # Sprite Groups
        self.g_all_sprites = pygame.sprite.Group()

        # Image groups
        self.images_mon = {}
        self.images_gui = {}
        self.images_otr = {}
        self.images_bld = {}

        # User Events
        # -> Resource Gain
        self.event_resource_gain = pygame.USEREVENT + 1
        pygame.time.set_timer(self.event_resource_gain, RESOURCE_GAIN_TIME)

        # Game States
        # FIXME - These are not yet used.
        self.game_states = {"building": False}

        # Start Up
        self.import_assets()

        # Create game classes and give them needed assets
        self.resource_mngr = ResourceManager()
        self.pop_mngr = PopulationManager()
        self.ui_mngr = UIManager(self.images_gui)
        self.monster_mngr = MonsterManager()
        self.building_mngr = BuildingManager(self.images_bld)

        self.setup()

    def import_assets(self):
        assets = u_import_assets()
        self.images_mon = assets.get("images_mon", None)
        self.images_gui = assets.get("images_gui", None)
        self.images_otr = assets.get("images_otr", None)
        self.images_bld = assets.get("images_bld", None)


    def setup(self):
        # This takes the MONSTER_CONFIG dict and replaces the image name with the actual image.
        # FIXME Move this to utils.py
        for monster_name, config in MONSTER_CONFIGS.items():
            config["image"] = self.images_mon[config.get("image")]


    def update(self):
        # FIXME - Game needs to go get all the info from it's managers and then parcel it out.
        self.building_mngr.update()


    def run(self) -> None:  # My need to change this later, part of a new code clarity
        while True:
            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == self.event_resource_gain:
                    pass

            # Game logic
            self.update()

            # Render
            # Clear the screen
            self.display_surface.fill((0, 0, 0))

            self.ui_mngr.render(self.display_surface, self.monster_mngr.monster_sprites)
            self.building_mngr.render(self.display_surface)

            pygame.display.update()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for frame rate
            # independent physics.
            self.dt = self.clock.tick(60) / 1000


if __name__ == '__main__':
    game = Game()
    game.run()
