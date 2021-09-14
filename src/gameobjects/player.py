import pygame as pg, os, paths, math, sprites
from gameobjects.map import Map
from gameobjects.powerup import Coffee
from gameobjects.shot import Shot

player_sprite_sheet = pg.image.load(os.path.join(paths.player_folder, 'player.png')).convert_alpha()


class Player(pg.sprite.Sprite):
    def __init__(self, map: Map):
        pg.sprite.Sprite.__init__(self)
        self.direction = 0
        self.step = 0
        self.image = pg.transform.scale(player_sprite_sheet.subsurface((0, 48 * self.direction), (25, 48)), (50, 96))
        self.shot_image = pg.transform.scale(pg.image.load(os.path.join(paths.player_folder, 'syringe.png')), (34, 14)).convert_alpha()
        self.rect = self.image.get_rect()
        self.hitbox = pg.Rect(self.rect.x, self.rect.y, self.rect.width - 16, self.rect.height - 16)
        self.rect.x = map.rect.width / 2 - self.rect.width / 2
        self.rect.y = map.rect.height / 2 - self.rect.height / 2
        self.map = map
        self.speed = 4.5
        self.shot_speed = 8
        self.shot_cooldown = 325
        self.last_shot = pg.time.get_ticks()

    def update(self):        
        key = pg.key.get_pressed()
        if key[pg.K_a] and key[pg.K_w]:
            self.rect.move_ip(round(-self.speed / 2 * math.sqrt(2)), round(-self.speed / 2 * math.sqrt(2)))
            self.direction = 1
        elif key[pg.K_a] and key[pg.K_s]:
            self.rect.move_ip(round(-self.speed / 2 * math.sqrt(2)), round(self.speed / 2 * math.sqrt(2)))
            self.direction = 1
        elif key[pg.K_d] and key[pg.K_w]:
            self.rect.move_ip(round(self.speed / 2 * math.sqrt(2)), round(-self.speed / 2 * math.sqrt(2)))
            self.direction = 2
        elif key[pg.K_d] and key[pg.K_s]:
            self.rect.move_ip(round(self.speed / 2 * math.sqrt(2)), round(self.speed / 2 * math.sqrt(2)))
            self.direction = 2
        elif key[pg.K_a]:
            self.rect.move_ip(-self.speed, 0)
            self.direction = 1
        elif key[pg.K_d]:
            self.rect.move_ip(self.speed, 0)
            self.direction = 2
        elif key[pg.K_w]:
            self.rect.move_ip(0, -self.speed)
            self.direction = 3
        elif key[pg.K_s]:
            self.rect.move_ip(0, self.speed)
            self.direction = 0

        self.image = pg.transform.scale(player_sprite_sheet.subsurface((0, 48 * self.direction), (25, 48)), (50, 96))

        if self.direction == 1 or self.direction == 2:
            self.hitbox.width = self.rect.width - 22
        else:
            self.hitbox.width = self.rect.width - 11

        self.rect = self.rect.clamp(self.map.rect)
        self.hitbox.center = self.rect.center

        if key[pg.K_LEFT] and key[pg.K_UP]:
            self.shoot(round(self.shot_speed / 2 * math.sqrt(2)), -1, -1, 135)
            self.direction = 1
        elif key[pg.K_LEFT] and key[pg.K_DOWN]:
            self.shoot(round(self.shot_speed / 2 * math.sqrt(2)), -1, 1, 225)
            self.direction = 1
        elif key[pg.K_RIGHT] and key[pg.K_UP]:
            self.shoot(round(self.shot_speed / 2 * math.sqrt(2)), 1, -1, 45)
            self.direction = 2
        elif key[pg.K_RIGHT] and key[pg.K_DOWN]:
            self.shoot(round(self.shot_speed / 2 * math.sqrt(2)), 1, 1, 315)
            self.direction = 2
        elif key[pg.K_LEFT]:
            self.shoot(self.shot_speed, -1, 0, 180)
            self.direction = 1
        elif key[pg.K_RIGHT]:
            self.shoot(self.shot_speed, 1, 0, 0)
            self.direction = 2
        elif key[pg.K_UP]:
            self.shoot(self.shot_speed, 0, -1, 90)
            self.direction = 3
        elif key[pg.K_DOWN]:
            self.shoot(self.shot_speed, 0, 1, 270)
            self.direction = 0

        for enemy in sprites.all_enemies:
            if self.hitbox.colliderect(enemy.hitbox):
                self.kill()

        for enemy_shot in sprites.all_enemy_shots:
            if self.hitbox.colliderect(enemy_shot.hitbox):
                self.kill()
                enemy_shot.kill()

        for powerup in sprites.all_powerups:
            if self.hitbox.colliderect(powerup.hitbox):
                if type(powerup) == Coffee:
                    self.speed = 5.5
                    powerup.kill()
        
    def shoot(self, shot_speed, horizontal_velocity, vertical_velocity, angle):
        current_shot = pg.time.get_ticks()
        if current_shot - self.last_shot >= self.shot_cooldown:
            self.last_shot = current_shot
            shot = Shot(self.shot_image, self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2, shot_speed, horizontal_velocity, vertical_velocity, angle, self.map)
            sprites.all_syringes.add(shot)
            sprites.all_sprites.add(shot)
