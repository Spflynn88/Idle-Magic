import pygame.draw
from pygame.sprite import Sprite
from settings import *

''' The UI will be  divided into different elements, each with there own class
    then the UI manager will create and manage them
    Each Panel will be a surface which uses sprite groups to draw to itself. Then UIM
    will draw the panels.
    
    These subclasses will talk ONLY to the UI which will talk ONLY to Game.
    
    UIM will also build a registry of buttons to make managing clicks easier.
    '''


class UIManager:
    _cls_images = None  # Image needed by the UI
    _cls_config = None  # The UI config file

    def __init__(self):
        self.sg_ui_elements = sprite_group()  # FIXME might not need a sprite group anymore
        self.g_ui_panels = {}  # List of all the panels, replaces the sprite group

        self.ui_build()

        self.g_button_register = sprite_group()
        self.get_all_buttons()


    @classmethod
    def load_settings(cls, t_images, t_config):
        cls._cls_images = t_images
        cls._cls_config = t_config

    def get_panel_by_name(self, t_name):
        return self.g_ui_panels[t_name]

    def get_all_buttons(self):
        """
    I'm not wild about this but here we are. This gets all the buttons from the panels and sub panels and
    gives them back to UIM. I did this so that I could actually use the buttons easier.
    """
        print("Getting all buttons from all panels")
        for name, panel in self.g_ui_panels.items():
            print(f"Processing panel: {name}")
            self.g_button_register.add(panel.get_buttons().sprites())
        print(f"Number of buttons registered: {len(self.g_button_register)}")

    def ui_build(self):
        # This is going to use the UI Config to assemble the UI
        for panel_name, config in UIManager._cls_config.items():
            self.g_ui_panels[panel_name] = UIPanel(
                config["pos"],
                config["width"],
                config["height"],
                config["color"],
                config["image"],
                config["buttons"]
            )

            # Handle sub-panels
            if "sub_panels" in config:
                self.g_ui_panels[panel_name].sub_panels = {}
                for sub_panel_name, sub_panel_config in config["sub_panels"].items():
                    sub_panel = UIPanel(
                        sub_panel_config["pos"],
                        sub_panel_config["width"],
                        sub_panel_config["height"],
                        sub_panel_config["color"],
                        sub_panel_config["image"],
                        sub_panel_config["buttons"]
                    )
                    self.g_ui_panels[panel_name].sub_panels[sub_panel_name] = sub_panel

    def update(self) -> None:
        # FIXME - This is going to work just like render() UIM calls the update on all it's children
        for name, panel in self.g_ui_panels.items():
            panel.update()

    def render(self, display_surface, *sprite_groups) -> None:
        for panel_name, panel in self.g_ui_panels.items():
            panel.render()
            display_surface.blit(panel.uip_display_surface, panel.pos)


class UIButton(Sprite):
    # The UI element that makes the button will pass it the needed action function
    # FIXME - make a defualt pic for easy protoing
    # FIXME - needs more properties to make it flexible (*args, **kwargs))
    def __init__(self, pos, t_image, t_group, callback=None):
        super().__init__(t_group)
        self.image = t_image
        self.rect = self.image.get_rect(topleft=pos)
        self.callback = callback

    def update(self):
        if self.rect.collidepoint(mouse_pos()):
            self.on_hover()

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
    _cls_images = None

    def __init__(self, t_pos, t_width=100, t_height=100, t_color='blue', t_image=None, t_buttons=None):
        # t_group is still used, but the group will not be a sprite group
        self.image = t_image  # The panel image - Not a sprite
        self.pos = t_pos

        # Sprite group to hold the sprites that make up the panel elements
        self.g_sprites = pygame.sprite.Group()
        self.g_sprites_btn = pygame.sprite.Group()
        self.sub_panels = {}

        if t_image:
            self.image_base = t_image  # Back up to replace when rendering
            self.uip_display_surface = pygame.Surface((self.image.width, self.image.height))
        else:
            # There is no image make a surface instead. Good for Testing
            self.color = t_color
            self.uip_display_surface = pygame.Surface((t_width, t_height))
            self.uip_display_surface.fill(t_color)

        if t_buttons:
            self.buttons_config = t_buttons  # Save the button config
            self.build_buttons()

    @classmethod
    def load_settings(cls, t_images):
        cls._cls_images = t_images

    def build_buttons(self):
        # Create any needed buttons
        for button, config in self.buttons_config.items():
            UIButton(
                config["pos"],
                UIPanel._cls_images[config["image"]].copy(),
                self.g_sprites_btn,
                config["callback"]
            )

    def get_buttons(self):
        # Create a group to hold all buttons in this panel and its sub-panels
        all_buttons = pygame.sprite.Group()

        # Add buttons from the current panel
        all_buttons.add(self.g_sprites_btn.sprites())

        # Recursively get buttons from all sub-panels
        for sub_panel in self.sub_panels.values():
            all_buttons.add(sub_panel.get_buttons().sprites())

        return all_buttons

    def update(self):
        if self.sub_panels:
            for panel in self.sub_panels.values():
                panel.update()
        if self.g_sprites:
            for sprite in self.g_sprites:
                sprite.update()


    def render(self):
        # Clear and blit the bg image
        if self.image:
            self.image = self.image_base.copy()
            self.uip_display_surface.blit(self.image, (0, 0))
        else:
            self.uip_display_surface.fill(self.color)

       # Call render for all the subpanels
        for sub_panel in self.sub_panels.values():
            sub_panel.render()
            # Blit the sub panel
            self.uip_display_surface.blit(sub_panel.uip_display_surface, sub_panel.pos)

        # Draw any sprites in the sprite group
        self.g_sprites.draw(self.uip_display_surface)
        self.g_sprites_btn.draw(self.uip_display_surface)