import pygame
from settings import *

# Alias
mouse_pos = pygame.mouse.get_pos


def u_import_assets():
    # FIXME - we need to seperate out all of the images and hand them to the correct manager
    images = {}
    for filename in listdir(SPRITE_FOLDER):
        if filename.endswith('.png'):
            image_name = os.path.splitext(filename)[0]
            image = pygame.image.load(os.path.join(SPRITE_FOLDER, filename)).convert_alpha()

            _key = str('images_' + image_name[:3])

            if _key in images:
                images[_key][image_name] = image
            else:
                images[_key] = {}
                images[_key][image_name] = image

        print(images)