import pygame, math, os, paths
from colors import white
from projectile import Projectile

player_sprite = pygame.transform.scale(pygame.image.load(os.path.join(paths.sprites_folder, 'ze-gotinha.png')), (34, 74))
projectile_sprite = pygame.image.load(os.path.join(paths.sprites_folder, 'syringe.png'))
syringes = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, sprites_group):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = player_sprite.convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = self.screen_rect.width / 2 - self.rect.width / 2
        self.rect.y = self.screen_rect.height / 2 - self.rect.height / 2
        self.sprites_group = sprites_group
        self.speed = 4
        self.diagonal_speed = (self.speed * math.sqrt(2)) / 2 + .5
        self.shot_speed = 10
        self.diagonal_shot_speed = (self.shot_speed * math.sqrt(2)) / 2
        self.last_shot = pygame.time.get_ticks()
        self.cooldown = 325
        self.current_direction = 'right'
        self.direction = 'right'

    def draw(self):
        pygame.draw.rect(self.screen, white, self.rect)

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
            
        if key[pygame.K_LEFT] and key[pygame.K_UP]:
            self.shoot(self.diagonal_shot_speed, -1, -1, 135)
        elif key[pygame.K_LEFT] and key[pygame.K_DOWN]:
            self.shoot(self.diagonal_shot_speed, -1, 1, 225)
        elif key[pygame.K_RIGHT] and key[pygame.K_UP]:
            self.shoot(self.diagonal_shot_speed, 1, -1, 45)
        elif key[pygame.K_RIGHT] and key[pygame.K_DOWN]:
            self.shoot(self.diagonal_shot_speed, 1, 1, 315)
        elif key[pygame.K_LEFT]:
            self.shoot(self.shot_speed, -1, 0, 180)
        elif key[pygame.K_RIGHT]:
            self.shoot(self.shot_speed, 1, 0, 0)
        elif key[pygame.K_UP]:
            self.shoot(self.shot_speed, 0, -1, 90)
        elif key[pygame.K_DOWN]:
            self.shoot(self.shot_speed, 0, 1, 270)

        self.rect = self.rect.clamp(self.screen.get_rect())

        if self.direction != self.current_direction:
            self.image = pygame.transform.flip(self.image, True, False)
            self.current_direction = self.direction

    def shoot(self, speed, horizontal_velocity, vertical_velocity, angle):
        current_shot = pygame.time.get_ticks()
        if current_shot - self.last_shot >= self.cooldown:
            self.last_shot = current_shot
            syringe = Projectile(self.screen, self.rect.center, speed, horizontal_velocity, vertical_velocity, angle, projectile_sprite.convert_alpha())
            self.sprites_group.add(syringe)
            syringes.add(syringe)
