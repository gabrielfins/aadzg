import pygame
from colors import white


class Text(pygame.sprite.Sprite):
    def __init__(self, screen, font, color, text):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.font = font
        self.color = color
        self.text = text
        self.text_surface = self.font.render(self.text, True, self.color)
        self.image = self.text_surface
        self.rect = self.image.get_rect()
        self.rect.right = self.surface.get_rect().width - 20
        self.rect.top = 20

    def draw(self):
        pygame.draw.rect(self.screen, white, self.rect)

    def update(self):
        self.text_surface = self.font.render(str(self.text), True, self.color)
        self.image = self.text_surface
        self.rect = self.image.get_rect()
        self.rect.right = self.surface.get_rect().width - 20
        self.rect.top = 20
