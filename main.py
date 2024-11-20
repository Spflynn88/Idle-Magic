import pygame

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

        # Image groups - these are forced below in import_assets but here to list what they should be
        self.images_mon = {}
        self.images_gui = {}
        self.images_otr = {}
        self.images_til = {}

        # User Events
        # -> Resource Gain - Not in use right now
        self.event_resource_gain = pygame.USEREVENT + 1
        pygame.time.set_timer(self.event_resource_gain, RESOURCE_GAIN_TIME)

        # Game States
        # FIXME - These are not yet used.
        self.game_states = {"building": False}
        '''There will be no base game state, if all others are false then it as at base.
        We can check for that like this:
        
        all_false = not any(my_dict.values())
        if all_false:
            print("All values are False!")

        '''

        # Start Up
        self.import_assets()
        self.setup()
        # DEBUG
        print(f"Number of til images {len(self.images_til)}")

        # Create game classes and give them needed assets
        self.mngr_resource = ResourceManager()
        self.mngr_pop = PopulationManager()
        self.mngr_ui = UIManager(self.images_gui)
        self.mngr_monster = MonsterManager()
        self.mngr_building = BuildingManager(self.images_til)

    def import_assets(self):
        assets = u_import_assets()
        # All the groups are listed in init, this won't throw an error if an image is mis-named
        for key in assets:
            setattr(self, key, assets[key])

    def setup(self):
        # This takes the MONSTER_CONFIG dict and replaces the image name with the actual image.
        # FIXME Move this to utils.py
        for monster_name, config in MONSTER_CONFIGS.items():
            config["image"] = self.images_mon[config.get("image")]

        print(f"waiting to convert nature tiles")
        for tile_name, config in TILE_CONFIGS_NATURE.items():
            # DEBUG
            # print(f"game.setup tile images {tile_name}, {config}")
            config["image"] = self.images_til[config.get("image")]
            config["image_h"] = self.images_til[config.get("image_h")]

    def update(self):
        # FIXME - Game needs to go get all the info from it's managers and then parcel it out.
        self.mngr_building.update()

    def run(self) -> None:  # My need to change this later, code clarity tag
        while True:
            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if not any(self.game_states.values()):
                    if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                        self.game_states = {key: False for key in self.game_states}
                        print(f"Esc key - game.game_states {self.game_states}")



            # Game logic
            self.update()

            # Render
            # Clear the screen
            self.display_surface.fill((0, 0, 0))

            self.mngr_ui.render(self.display_surface)
            self.mngr_building.render(self.display_surface)

            pygame.display.update()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for frame rate
            # independent physics.
            self.dt = self.clock.tick(60) / 1000


if __name__ == '__main__':
    game = Game()
    game.run()
