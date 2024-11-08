from settings import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, group):
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_frect(topleft=pos)


class Button(Sprite):
    def __init__(self, pos, surf, group, action):
        super().__init__(pos, surf, group)
        self.action = action

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action: self.action()
        return False
