from settings import *
from os import listdir


def u_import_assets():
    # Loads all the .png files then separates them into dictionaries by the 3-letter code.
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

    return images

def u_images_to_config(t_images_mon, t_images_til):
    for monster_name, config in MONSTER_CONFIGS.items():
        config["image"] = t_images_mon[config.get("image")]

    for tile_name, config in TILE_CONFIGS_NATURE.items():
        # DEBUG
        # print(f"game.setup tile images {tile_name}, {config}")
        config["image"] = t_images_til[config.get("image")]
        config["image_h"] = t_images_til[config.get("image_h")]
