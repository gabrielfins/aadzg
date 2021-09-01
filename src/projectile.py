import pygame
from colors import white


class Projectile(pygame.sprite.Sprite):
    def __init__(self, screen, center, speed, horizontal_velocity, vertical_velocity, angle, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(sprite, angle)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.screen = screen
        self.speed = speed
        self.horizontal_velocity = horizontal_velocity
        self.vertical_velocity = vertical_velocity
        
    def draw(self):
        pygame.draw.rect(self.screen, white, self.rect)

    def update(self):
        self.rect.move_ip(self.speed * self.horizontal_velocity, self.speed * self.vertical_velocity)

        if (self.rect.x + self.rect.width < 0 or
            self.rect.x > self.screen.get_rect().width or
            self.rect.y + self.rect.height < 0 or
            self.rect.y > self.screen.get_rect().height):
            self.kill()
