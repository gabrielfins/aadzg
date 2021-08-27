import pygame
from colors import WHITE
import os

game_folder = os.path.dirname(__file__)
sprites_folder = os.path.join(game_folder, 'sprites')

projectile_sprite = pygame.image.load(os.path.join(sprites_folder, 'syringe.png'))


class Projectile(pygame.sprite.Sprite):
    def __init__(self, surface, center, speed, rotation):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(projectile_sprite.convert_alpha(), rotation)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = speed
        self.rotation = rotation
        self.surface = surface
        self.surface_rect = surface.get_rect()

    def draw(self):

        pygame.draw.rect(self.surface, WHITE, self.rect)

    def update(self):
        self.rect.move_ip(self.speed)

        if (self.rect.x + self.rect.width < 0 or
                self.rect.x > self.surface_rect.width or
                self.rect.y + self.rect.height < 0 or
                self.rect.y > self.surface_rect.height):
            self.kill()
