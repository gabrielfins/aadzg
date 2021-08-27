import math
import pygame
import os
from colors import WHITE
from projectile import Projectile

game_folder = os.path.dirname(__file__)
sprites_folder = os.path.join(game_folder, 'sprites')

player_sprite = pygame.image.load(os.path.join(sprites_folder, 'character.png'))

syringes = pygame.sprite.Group()


class Character(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, sprite_group):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_sprite.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.width / 2, self.rect.height / 2)
        self.rect.x = x / 2 - self.rect.width / 2
        self.rect.y = y / 2 - self.rect.height / 2
        self.speed = 4
        self.diagonal_speed = (self.speed * math.sqrt(2)) / 2 + .5
        self.shot_speed = 10
        self.diagonal_shot_speed = (self.shot_speed * math.sqrt(2)) / 2
        self.sprite_group = sprite_group
        self.surface = surface
        self.surface_rect = surface.get_rect()
        self.last_shot = pygame.time.get_ticks()
        self.cooldown = 325
        self.current_direction = 'right'
        self.direction = 'right'
        self.doses = 25

    def draw(self):
        pygame.draw.rect(self.surface, WHITE, self.rect)

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and key[pygame.K_w]:
            self.rect.move_ip(-self.diagonal_speed, -self.diagonal_speed)
            self.direction = 'left'
        elif key[pygame.K_a] and key[pygame.K_s]:
            self.rect.move_ip(-self.diagonal_speed, self.diagonal_speed)
            self.direction = 'left'
        elif key[pygame.K_d] and key[pygame.K_w]:
            self.rect.move_ip(self.diagonal_speed, -self.diagonal_speed)
            self.direction = 'right'
        elif key[pygame.K_d] and key[pygame.K_s]:
            self.rect.move_ip(self.diagonal_speed, self.diagonal_speed)
            self.direction = 'right'
        elif key[pygame.K_a]:
            self.rect.move_ip(-1 * self.speed, 0)
            self.direction = 'left'
        elif key[pygame.K_d]:
            self.rect.move_ip(1 * self.speed, 0)
            self.direction = 'right'
        elif key[pygame.K_w]:
            self.rect.move_ip(0, -1 * self.speed)
        elif key[pygame.K_s]:
            self.rect.move_ip(0, 1 * self.speed)
        elif key[pygame.K_F1]:
            self.rect.x = self.surface_rect.width / 2 - self.rect.width / 2
            self.rect.y = self.surface_rect.height / 2 - self.rect.height / 2

        self.rect = self.rect.clamp(self.surface_rect)

        if self.direction != self.current_direction:
            self.image = pygame.transform.flip(self.image, True, False)
            self.current_direction = self.direction

    def shoot(self, direction):
        if self.doses > 0:
            current_shot = pygame.time.get_ticks()
            if current_shot - self.last_shot >= self.cooldown:
                syringe = None
                self.last_shot = current_shot
                if direction == 'left':
                    syringe = Projectile(self.surface, self.rect.center, (-10, 0), 180)
                    self.direction = 'left'
                elif direction == 'right':
                    syringe = Projectile(self.surface, self.rect.center, (10, 0), 0)
                    self.direction = 'right'
                elif direction == 'up':
                    syringe = Projectile(self.surface, self.rect.center, (0, -10), 90)
                elif direction == 'down':
                    syringe = Projectile(self.surface, self.rect.center, (0, 10), 270)
                elif direction == 'left up':
                    syringe = Projectile(self.surface, self.rect.center, (-7, -7), 135)
                elif direction == 'left down':
                    syringe = Projectile(self.surface, self.rect.center, (-7, 7), -135)
                elif direction == 'right up':
                    syringe = Projectile(self.surface, self.rect.center, (7, -7), 45)
                elif direction == 'right down':
                    syringe = Projectile(self.surface, self.rect.center, (7, 7), -45)

                self.sprite_group.add(syringe)
                syringes.add(syringe)
                self.doses -= 1
