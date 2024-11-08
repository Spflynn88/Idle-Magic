import pygame.sprite

from settings import *
from sys import exit
from entities import *

from resources import ResourceManager, PopulationManager
from monster import MonsterManager
from ui import UIManager
#from spells import SpellManager
#from utils import load_image, load_sound

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

        # Sprite Groups
        self.g_all_sprites = pygame.sprite.Group()

        # Image groups
        self.images_monsters = {}
        self.images_ui = {}
        self.images_other = {}


        # User Events
        # -> Resource Gain
        self.event_resource_gain = pygame.USEREVENT + 1
        pygame.time.set_timer(self.event_resource_gain, RESOURCE_GAIN_TIME)

        # Start Up
        self.import_assets()

        # Create game classes and give them needed assets
        self.resource_mngr = ResourceManager()
        self.pop_mngr = PopulationManager()
        self.ui_mngr = UIManager(self.images_ui)
        self.monster_mngr = MonsterManager()

        self.setup()

    def import_assets(self):
        # FIXME - we need to sperate out all of the images and hand them to the correct manager
        # this can probably move to utils also
        for filename in listdir(SPRITE_FOLDER):
            if filename.endswith('.png'):
                image_name = os.path.splitext(filename)[0]
                image = pygame.image.load(os.path.join(SPRITE_FOLDER, filename)).convert_alpha()

                # Seperate out monster images
                if image_name[:3] == 'mon':
                    self.images_monsters[image_name] = image
                # UI images
                elif image_name[:3] == 'ui_':
                    self.images_ui[image_name] = image

                # Catch all else
                else:
                    self.images_other[image_name] = image


    def setup(self):
        # This takes the MONSTER_CONFIGs and replaces the image name with the actual image.
        # FIXME Move this to utils.py
        for monster_name, config in MONSTER_CONFIGS.items():
            config["image"] = self.images_monsters[config.get("image")]

        self.monster_mngr.add_monster("Mana_Imp", (25, 25))

    def update(self, t_mon_yield):
        # FIXME - Game needs to go get all the info from it's managers and then parcel it out.
        resource_count = self.resource_mngr.update(t_mon_yield)
        self.ui_mngr.update(resource_count)

    # Button functions

    def run(self) -> None:  # My need to change this later, part of a new code clarity initiate

        while True:
            mon_yield = (0, 0, 0) # FIXME this is not right rework
            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == self.event_resource_gain:
                    mon_yield = self.monster_mngr.calc_resource_yield()


            # Game logic
            self.update(mon_yield)

            # Render
            # Clear the screen
            self.display_surface.fill((0, 0, 0))

            # All Managers draw their sprites
            self.ui_mngr.render(self.display_surface)
            self.monster_mngr.render(self.display_surface)


            pygame.display.update()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for frame rate
            # independent physics.
            self.dt = self.clock.tick(60) / 1000


if __name__ == '__main__':
    game = Game()
    game.run()