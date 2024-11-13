import pygame
from pygame.sprite import Sprite
from settings import *

#FIXME - the UI also needs to be handed all of it's out image files
''' The UI will be  divided into different elements, each with there own class
    then the UI manager will create and manage them
    Each element will have an update and render method.
    
    These subclasses will talk ONLY to the UI which will talk ONLY to Game.
    '''


class UIManager:
    def __init__(self, t_ui_images):
        self.g_ui_elements = pygame.sprite.Group()
        self.ui_images = t_ui_images

        # UI creates all of its elements
        self.resource_panel = ResourcesPanel(UI_RESOURCE_BAR_POS, self.ui_images["ui_resource_bar"], self.g_ui_elements)

    def update(self, t_resource_count):
        # called from Game
        # self.healthbar.update() <- example
        self.resource_panel.update(t_resource_count) # FIXME - proper values

    def render(self, display_surface):
        # FIXME This is a stretch but the UI should only update - see performance notes
        # if all the ui is in the sprite group then just draw that sprite group for now i guess
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
        super().__init__(group)
        self.image = t_image
        self.image_base = t_image
        self.rect = self.image.get_rect(center=pos)

        self.font = pygame.font.Font(None, 36)
        self.text = "Start"
        self.color = (0,0,0)
        self.text_pos = (88, 26)
        self.text_surf = self.font.render(self.text, True, self.color)

    def update(self, t_resources):
        # Wipe Surface
        self.image = self.image_base.copy()

        # Update Surface
        self.text = f"{t_resources.mana:<32}{t_resources.essence}" # Update the text
        self.text_surf = self.font.render(self.text, True, self.color) # Update the text surface
        self.image.blit(self.text_surf, self.text_pos)

    def render(self):
        pass
    # Still don't need render. Sprite draw works fine, I'm just blit-ing the text onto its own image

