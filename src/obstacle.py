import pygame, os, paths
from colors import white

obstacle_sprite = pygame.transform.scale2x(pygame.image.load(os.path.join(paths.sprites_folder, 'tree.png')))


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = obstacle_sprite.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self):
        pygame.draw.rect(self.screen, white, self.rect)
