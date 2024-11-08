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

    def update(self):
        # called from Game
        # self.healthbar.update() <- example
        self.resource_panel.update()
        pass

    def render(self, display_surface):
        # FIXME This is a stretch but the UI should only update - see performance notes
        # if all the ui is in the sprite group then just draw that sprite group for now i guess
        #self.resource_panel.render()
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
        self.rect = self.image.get_rect(center=pos)
        print("class ResourcesPanel - created")

    def update(self):
        pass
