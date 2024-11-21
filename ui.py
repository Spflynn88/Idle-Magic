from pygame.sprite import Sprite
from settings import *

''' The UI will be  divided into different elements, each with there own class
    then the UI manager will create and manage them
    Each Panel will be a surface which uses sprite groups to draw to itself. Then UIM
    will draw the panels.
    
    These subclasses will talk ONLY to the UI which will talk ONLY to Game.
    '''


class UIManager:
    def __init__(self, t_ui_images):
        self.sg_ui_elements = pygame.sprite.Group()  # FIXME might not need a sprite group anymore
        self.g_ui_panels = []  # List of all the panels, replaces the sprite group
        self._ui_images = t_ui_images  # List of the images needed for the UI

        # FIXME - what if here we dispense the needed images to the sub-classes then t_ui_images doesn't need to be saved

        # UI creates all of its elements - create panel - add panel to g_ui_panels
        # Side Panel
        self.ui_panel_side = UISidePanel((0, 0), UI_SIDE_PANEL_W, UI_SIDE_PANEL_H, 'gray')
        self.g_ui_panels.append(self.ui_panel_side)
        # Resource Panel
        self.ui_panel_resource = UIPanel(UI_RESOURCE_BAR_POS, SCREEN_WIDTH - UI_SIDE_PANEL_W,
                                         50, 'blue')
        self.g_ui_panels.append(self.ui_panel_resource)

    def update(self, t_resource_count) -> None:
        # FIXME - This is going to work just like render() UIM calls the update on all it's children
        # called from Game, takes Resource()
        pass

    def render(self, display_surface, *sprite_groups) -> None:
        for element in self.g_ui_panels:
            element.render()
            display_surface.blit(element.uip_display_surface, element.pos)


class UIButton(Sprite):
    # The UI element that makes the button will pass it the needed action function
    # FIXME - make a defualt pic for easy protoing
    # FIXME - needs more properties to make it flexible (*args, **kwargs))
    def __init__(self, pos, t_image, group, callback=None):
        super().__init__(group)
        self.image = t_image
        self.rect = self.image.get_rect(topleft=pos)
        self.callback = callback

    def update(self):
        pass

    def on_hover(self):
        pass

    def handel_event(self, t_event):
        # on_click calls the callback, but this should still be here
        if t_event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(t_event.pos):
                self.on_click(t_event)

    def on_click(self, t_event):
        print(f"Button event: {t_event}")
        self.callback()


class UIPanel:
    def __init__(self, t_pos, t_width=100, t_height=100, t_color='blue', t_image=None,):
        # t_group is still used, but the group will not be a sprite group
        self.image = t_image  # The panel image - Not a sprite

        if t_image:
            self.image_base = t_image  # Back up to replace when rendering
            self.uip_display_surface = pygame.Surface((self.image.width, self.image.height))
        else:
            # There is no image make a surface instead. Good for Testing
            self.color = t_color
            self.uip_display_surface = pygame.Surface((t_width, t_height))
            self.uip_display_surface.fill(t_color)

        self.pos = t_pos

        # Sprite group to hold the sprites that make up the panel elements
        self.g_sprites = pygame.sprite.Group()
        self.sub_panels = []
        self.build()

    def build(self):
        # Create all the elements needed for the panel
        pass

    def render(self):
        # Clear and blit the bg image
        if self.image:
            self.image = self.image_base.copy()
            self.uip_display_surface.blit(self.image, (0, 0))
        else:
            self.uip_display_surface.fill(self.color)

       # Call render for all the subpanels
        for sub_panel in self.sub_panels:
            sub_panel.render()
            # Blit the sub panel
            self.uip_display_surface.blit(sub_panel.uip_display_surface, sub_panel.pos)

        # Draw any sprites in the sprite group
        self.g_sprites.draw(self.uip_display_surface)


class UISidePanel(UIPanel):
    def __init__(self, t_pos, t_width=100, t_height=100, t_color='gray', t_image=None):
        # Initialize the base UIPanel
        super().__init__(t_pos, t_width, t_height, t_color, t_image)

        self.sub_panels = [self.ui_sp_build_panel] # UI Side Panel

    def build(self):
        print("Building UISidePanel")
        self.ui_sp_build_panel = UIPanel((0, 0), t_color='red')
        self.sub_panels.append(self.ui_build_panel)

    def render(self):
        super().render()  # Render this panel
        # Render the sub_panels
        for sub_panel in self.sub_panels:
            sub_panel.render()
            self.uip_display_surface.blit(sub_panel.uip_display_surface, sub_panel.pos)