import pygame
import os
from colors import WHITE

game_folder = os.path.dirname(__file__)
sprites_folder = os.path.join(game_folder, 'sprites')

recharge_sprite = pygame.image.load(os.path.join(sprites_folder, 'recharge.png'))


class Recharge(pygame.sprite.Sprite):
    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(recharge_sprite.convert_alpha(), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20
        self.surface = surface

    def draw(self):
        pygame.draw.rect(self.surface, WHITE, self.rect)
