import pygame.sprite

from settings import *
from sys import exit
from entities import *

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

        self.sprites = {}  # General sprites dict by file name

        # Sprite Groups
        self.all_sprites = pygame.sprite.Group()

        # User Events

        # Start Up
        self.import_assets()
        self.setup()

    def import_assets(self):
        for filename in listdir(SPRITE_FOLDER):
            if filename.endswith('.png'):
                sprite_name = os.path.splitext(filename)[0]
                sprite_image = pygame.image.load(os.path.join(SPRITE_FOLDER, filename)).convert_alpha()
                self.sprites[sprite_name] = sprite_image

    def setup(self):
        pass

    def update(self):
        for sprite in self.all_sprites:
            sprite.update()

    def run(self) -> None:  # My need to change this later, part of a new code clarity initiate

        while True:
            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            # Game logic
            self.update()

            # Render
            # Clear the screen
            self.display_surface.fill((0, 0, 0))
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for frame rate
            # independent physics.
            self.dt = self.clock.tick(60) / 1000


if __name__ == '__main__':
    game = Game()
    game.run()