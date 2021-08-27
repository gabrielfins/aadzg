import pygame
import os
from character import Character
from colors import WHITE

game_folder = os.path.dirname(__file__)
fonts_folder = os.path.join(game_folder, 'fonts')


class Text(pygame.sprite.Sprite):
    def __init__(self, surface, text, size, color, player: Character):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.text = text
        self.font = pygame.font.Font(os.path.join(fonts_folder, 'PatuaOne-Regular.ttf'), size)
        self.color = color
        self.text_surface = self.font.render(self.text, True, self.color)
        self.image = self.text_surface
        self.rect = self.image.get_rect()
        self.rect.right = self.surface.get_rect().width - 20
        self.rect.top = 20
        self.player = player

    def draw(self):
        pygame.draw.rect(self.surface, WHITE, self.rect)

    def update(self):
        self.text = self.player.doses
        self.text_surface = self.font.render(f'{self.text}', True, self.color)
        self.image = self.text_surface
        self.rect = self.image.get_rect()
        self.rect.right = self.surface.get_rect().width - 20
        self.rect.top = 20
