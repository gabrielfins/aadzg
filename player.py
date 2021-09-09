import pygame as pg, sprites, os, paths, math
from shot import Shot


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.width = 34
        self.height = 80
        self.image = pg.transform.scale(pg.image.load(os.path.join(paths.images_folder, 'player.png')), (self.width, self.height)).convert_alpha()
        self.shot_image = pg.transform.scale(pg.image.load(os.path.join(paths.images_folder, 'syringe.png')), (34, 14)).convert_alpha()
        self.rect = self.image.get_rect()
        self.hitbox = pg.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height - 40)
        self.rect.x = sprites.map.rect.width / 2 - self.rect.width / 2
        self.rect.y = sprites.map.rect.height / 2 - self.rect.height / 2
        self.speed = 4.5
        self.shot_speed = 8
        self.shot_cooldown = 325
        self.last_shot = pg.time.get_ticks()

    def update(self):        
        key = pg.key.get_pressed()
        if key[pg.K_a] and key[pg.K_w]:
            self.rect.move_ip(round(-self.speed / 2 * math.sqrt(2)), round(-self.speed / 2 * math.sqrt(2)))
        elif key[pg.K_a] and key[pg.K_s]:
            self.rect.move_ip(round(-self.speed / 2 * math.sqrt(2)), round(self.speed / 2 * math.sqrt(2)))
        elif key[pg.K_d] and key[pg.K_w]:
            self.rect.move_ip(round(self.speed / 2 * math.sqrt(2)), round(-self.speed / 2 * math.sqrt(2)))
        elif key[pg.K_d] and key[pg.K_s]:
            self.rect.move_ip(round(self.speed / 2 * math.sqrt(2)), round(self.speed / 2 * math.sqrt(2)))
        elif key[pg.K_a]:
            self.rect.move_ip(-self.speed, 0)
        elif key[pg.K_d]:
            self.rect.move_ip(self.speed, 0)
        elif key[pg.K_w]:
            self.rect.move_ip(0, -self.speed)
        elif key[pg.K_s]:
            self.rect.move_ip(0, self.speed)

        self.rect = self.rect.clamp(sprites.map.rect)

        self.hitbox.x = self.rect.x
        self.hitbox.bottom = self.rect.bottom

        if key[pg.K_LEFT] and key[pg.K_UP]:
            self.shoot(round(self.shot_speed / 2 * math.sqrt(2)), -1, -1, 135)
        elif key[pg.K_LEFT] and key[pg.K_DOWN]:
            self.shoot(round(self.shot_speed / 2 * math.sqrt(2)), -1, 1, 225)
        elif key[pg.K_RIGHT] and key[pg.K_UP]:
            self.shoot(round(self.shot_speed / 2 * math.sqrt(2)), 1, -1, 45)
        elif key[pg.K_RIGHT] and key[pg.K_DOWN]:
            self.shoot(round(self.shot_speed / 2 * math.sqrt(2)), 1, 1, 315)
        elif key[pg.K_LEFT]:
            self.shoot(self.shot_speed, -1, 0, 180)
        elif key[pg.K_RIGHT]:
            self.shoot(self.shot_speed, 1, 0, 0)
        elif key[pg.K_UP]:
            self.shoot(self.shot_speed, 0, -1, 90)
        elif key[pg.K_DOWN]:
            self.shoot(self.shot_speed, 0, 1, 270)

        for powerup in sprites.all_powerups:
            if self.hitbox.colliderect(powerup.hitbox):
                self.speed = 7.5
                powerup.kill()

        for enemy in sprites.all_enemies:
            if self.hitbox.colliderect(enemy.hitbox):
                self.die()

        for enemy_shot in sprites.all_enemy_shots:
            if self.hitbox.colliderect(enemy_shot.hitbox):
                self.die()
        
    def shoot(self, shot_speed, horizontal_velocity, vertical_velocity, angle):
        current_shot = pg.time.get_ticks()
        if current_shot - self.last_shot >= self.shot_cooldown:
            self.last_shot = current_shot
            shot = Shot(self.shot_image, self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2, shot_speed, horizontal_velocity, vertical_velocity, angle)
            sprites.all_syringes.add(shot)
            sprites.all_sprites.add(shot)

    def die(self):
        self.kill()