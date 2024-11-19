from settings import *


class BuildingManager:
    # The building manager will display the building grid and manage it.
    def __init__(self, t_images_bld):
        self._images_bld = t_images_bld

        # DEGUB
        print("Checking bld images")
        for key in self._images_bld:
            print(f"Key image {key}")

        self.g_building_sprites = pygame.sprite.Group()
        self.building_grid = BuildingGrid(self._images_bld, self.g_building_sprites)

    def update(self):
        self.building_grid.update()

    def render(self, t_display_surface):
        # STD pattern the manager calls the render of its children, then draws its own group
        self.building_grid.render()

        self.g_building_sprites.draw(t_display_surface)


class BuildingGrid(pygame.sprite.Sprite):
    def __init__(self, t_bld_images, t_group):
        super().__init__(t_group)
        self.grid_rows = BUILD_GRID_ROWS
        self.grid_cols = BUILD_GRID_COLS
        self.tile_size = BUILD_GRID_TILE

        self._bld_images = t_bld_images  # Images of the needed buildings and tiles

        # I don't want every grid tile checking every tick, so this is going to help point to the needed one.
        self.offset_x = BUILD_GRID_START_POS[0]
        self.offset_y = BUILD_GRID_START_POS[1]

        # Create the Surface
        self.image = pygame.Surface((self.grid_cols * self.tile_size,
                                     self.grid_rows * self.tile_size))
        self.rect = self.image.get_frect(topleft=BUILD_GRID_START_POS)

        # Create the grid
        self.g_grid_tiles = pygame.sprite.Group()
        self._grid = self.generate_grid()

    def generate_grid(self):
        final_grid = []  # The final grid containing all rows
        for col in range(self.grid_cols):  # Iterate through grid columns
            row_grid = []  # Reset the row grid for the current column
            for row in range(self.grid_rows):  # Iterate through grid rows
                _new_tile = GridTile(
                    (col * self.tile_size, row * self.tile_size),  # Position
                    self._bld_images["bld_grd_tile"],  # Tile image
                    self.g_grid_tiles,  # Tile group
                    (col, row)
                )
                row_grid.append(_new_tile)
            final_grid.append(row_grid)
        return final_grid

    def update(self):
        # Check if the mouse is over the grid, then find the tile id
        if self.rect.collidepoint(mouse_pos()):
            # Adjust the mouse_pos by the offset
            tile_id_x = (mouse_pos()[0] - self.offset_x) // self.tile_size
            tile_id_y = (mouse_pos()[1] - self.offset_y) // self.tile_size

            self._grid[tile_id_x][tile_id_y].highlight(self._bld_images["bld_grd_htile"])

    def render(self):
        self.image.fill('black')
        self.g_grid_tiles.draw(self.image)


class GridTile(pygame.sprite.Sprite):
    '''
    These need to be made with the default tile image being given first. It saves it as the defualt. I'm not sure this
    is great though as it makes it less flexible.
    '''
    def __init__(self, t_pos, t_image, t_groups, t_tile_id):
        super().__init__(t_groups)
        self.image_default = t_image
        self.image = t_image
        self.rect = self.image.get_frect(topleft=t_pos)
        self.tile_id = t_tile_id

        self.hl_dirty = False  # This changes when the tile gets high-lighted then is used to reset.

    def update(self):
        pass

    def highlight(self, t_image):
        self.image = t_image

class Building:
    # Individual buildings
    pass





