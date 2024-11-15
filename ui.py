import pygame
from pygame.sprite import Sprite
from settings import *

#FIXME - give the UI is own surface, then use colorKey to fix transperency
''' The UI will be  divided into different elements, each with there own class
    then the UI manager will create and manage them
    Each element will have an update and render method.
    
    These subclasses will talk ONLY to the UI which will talk ONLY to Game.
    '''


class UIManager:
    def __init__(self, t_ui_images):
        self.g_ui_elements = pygame.sprite.Group()
        self._ui_images = t_ui_images

        # UI creates all of its elements
        self.resource_panel = ResourcesPanel(UI_RESOURCE_BAR_POS, self._ui_images["ui_resource_bar"], self.g_ui_elements)
        self.monster_roster = MonsterRoster(UI_MON_ROSTER_POS,
                                            self._ui_images["ui_monster_roster"],
                                            self._ui_images["ui_mon_frame"],
                                            self.g_ui_elements)

    def update(self, t_resource_count) -> None:
        # called from Game, takes Resource()
        # self.healthbar.update() <- example
        self.resource_panel.update(t_resource_count) # FIXME - proper values

    def render(self, display_surface, t_sprites_monsters, *sprite_groups) -> None:
        # FIXME The UI elements are Sprites or surfaces, they are going to build themselves and UIMan will render them
        # Build the UI elements
        self.monster_roster.render(t_sprites_monsters)

        # Draw the UI
        self.g_ui_elements.draw(display_surface)


class UIButton(Sprite):
    # The UI element that makes the button will pass it the needed action function
    def __init__(self, pos, t_image, group, action=None):
        super().__init__(group)
        self.image = t_image
        self.rect = self.image.get_rect(topleft=pos)
        self.action = action

    def update(self):
        pass

    def on_hover(self):
        pass

    def handel_event(self, event):
        pass

    def on_click(self, event):
        pass


class ResourcesPanel(Sprite):
    def __init__(self, pos, t_image, group):
        # FIXME - Make a UI element parent class? Could include font but maybe not size?
        super().__init__(group)
        self.image = t_image
        self.image_base = t_image
        self.rect = self.image.get_frect(midtop=pos)

        self.font = pygame.font.Font(None, 36)
        self.text = "Start"
        self.color = (0,0,0)
        self.text_pos = (88, 26)
        self.text_surf = self.font.render(self.text, True, self.color)

    def update(self, t_resources) -> None:
        # FIXME - some slop here, update and render need to be discussed
        # Takes Resource()
        # Wipe Surface
        self.image = self.image_base.copy()

        # Update Surface
        self.text = f"{t_resources.vpearls:<32}{t_resources.essence}" # Update the text
        self.text_surf = self.font.render(self.text, True, self.color) # Update the text surface
        self.image.blit(self.text_surf, self.text_pos)

    def render(self):
        pass


class MonsterRoster(Sprite):
    def __init__(self, pos, t_image, t_frame, group):
        super().__init__(group)
        self.image = t_image
        self.image_default = t_image
        self.rect = self.image.get_frect(topleft=pos)

        self.frame = t_frame

        # FIXME - change all this to be dynamic
        # Panel layout
        self._top_margin = int(.06 * self.rect.height)   # This is distance from the top we want to start placing things
        self._icon_margin = int(.06 * self.rect.height)  # Distance between Monsters
        # FIXME - change the frame to have a % border size to calculate the offset
        self._frame_offset = 18 # X and Y offset for the fame

    def build_monster_frames(self):
        # IDK about this yet.
        pass

    def update(self):
        pass

    def render(self, t_sprites_monsters):
        for count, monster in enumerate(t_sprites_monsters):
            monster.rect.x = self.rect.width // 2 - monster.rect.width // 2
            monster.rect.y = self._top_margin + (self._icon_margin + monster.rect.height) * count

            self.image.blit(monster.image, monster.rect)
            self.image.blit(self.frame, (monster.rect.x - self._frame_offset, monster.rect.y - self._frame_offset))



