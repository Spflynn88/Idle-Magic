from settings import *


class BuildingManager:
    # The building manager will display the building grid and manage it.
    def __init__(self):
        self.g_building_sprites = pygame.sprite.Group()
        self.building_grid = BuildingGrid(self.g_building_sprites)

    def update(self):
        self.building_grid.update()

    def render(self, t_display_surface):
        self.building_grid.render()

        self.g_building_sprites.draw(t_display_surface)


class BuildingGrid(pygame.sprite.Sprite):
    def __init__(self, t_group):
        super().__init__(t_group)
        self.grid_rows = BUILD_GRID_ROWS
        self.grid_cols = BUILD_GRID_COLS
        self.tile_size = BUILD_GRID_TILE

        self.line_width = 2
        self.line_color = 'gray'

        # Create the offset from 0,0 so that the mouse_pos can figure out which tile it's over
        self.offset_x = BUILD_GRID_START_POS[0]
        self.offset_y = BUILD_GRID_START_POS[1]

        # Create the Surface
        self.image = pygame.Surface((self.grid_cols * self.tile_size + self.line_width,
                                     self.grid_rows * self.tile_size + self.line_width))
        self.rect = self.image.get_frect(topleft=BUILD_GRID_START_POS)

        # Setup color key
        self.image.fill('green')
        self.image.set_colorkey('green')
        self.image.set_alpha(255 // 2)

        # Setup highlighting
        self.hl_surf = pygame.Surface((self.tile_size, self.tile_size))
        self.hl_surf.fill('gray')
        self.hl_check = False
        self.hl_pos = ()

    def generate_grid(self):
        pass

    def update(self):
        # Check if the mouse is over the grid, then find the tile id
        if self.rect.collidepoint(mouse_pos()):
            # Adjust the mouse_pos by the offset
            tile_id_x = (mouse_pos()[0] - self.offset_x) // self.tile_size
            tile_id_y = (mouse_pos()[1] - self.offset_y) // self.tile_size
            # DEBUG
            print(f"Tile id {tile_id_x},{tile_id_y}")

            # Get the position of the corner of the tile
            hl_pos_x = tile_id_x * self.tile_size
            hl_pos_y = tile_id_y * self.tile_size
            self.hl_check = True
            self.hl_pos = (hl_pos_x, hl_pos_y)

    def render(self):
        self.image.fill('green')
        pos_y = 0
        pos_x = 0
        # Draw grid lines
        for row in range(self.grid_rows + 1):
            pygame.draw.line(self.image, self.line_color, (0, pos_y), (self.image.get_width(), pos_y))
            pos_y += self.tile_size
        for col in range(self.grid_cols + 1):
            pygame.draw.line(self.image, self.line_color, (pos_x, 0), (pos_x, self.image.get_height()))
            pos_x += self.tile_size

        if self.hl_check:
            self.image.blit(self.hl_surf, self.hl_pos)

class Building:
    # Individual buildings
    pass





