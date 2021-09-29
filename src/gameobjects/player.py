import pygame as pg, os, paths, math, sprites
from gameobjects.map import Map
from gameobjects.powerup import Coffee
from gameobjects.shot import Shot

player_sprite_sheet = pg.image.load(os.path.join(paths.player_folder, 'player.png')).convert_alpha()
shot_sprite = pg.image.load(os.path.join(paths.player_folder, 'syringe.png')).convert_alpha()


class Player(pg.sprite.Sprite):
    def __init__(self, map: Map):
        pg.sprite.Sprite.__init__(self)
        self.direction = 0
        self.step = 0
        self.image = pg.transform.scale(player_sprite_sheet.subsurface((0, 48 * self.direction), (25, 48)), (50, 96))
        self.rect = self.image.get_rect()
        self.rect.x = map.rect.width / 2 - self.rect.width / 2
        self.rect.y = map.rect.height / 2 - self.rect.height / 2
        self.hitbox = pg.Rect(self.rect.x, self.rect.y, self.rect.width - 16, self.rect.height - 52)
        self.map = map
        self.speed = 4
        self.shot_speed = 8
        self.shot_cooldown = 325
        self.last_shot = pg.time.get_ticks()
        self.lives = 3
        self.iframes = 2500
        self.last_hit = pg.time.get_ticks()

    def update(self):
        key = pg.key.get_pressed()

        if key[pg.K_a] and key[pg.K_w]:
            self.rect.move_ip(round(-self.speed * math.sqrt(2) / 2), round(-self.speed * math.sqrt(2) / 2))
            self.direction = 1
        elif key[pg.K_a] and key[pg.K_s]:
            self.rect.move_ip(round(-self.speed * math.sqrt(2) / 2), round(self.speed * math.sqrt(2) / 2))
            self.direction = 1
        elif key[pg.K_d] and key[pg.K_w]:
            self.rect.move_ip(round(self.speed * math.sqrt(2) / 2), round(-self.speed * math.sqrt(2) / 2))
            self.direction = 2
        elif key[pg.K_d] and key[pg.K_s]:
            self.rect.move_ip(round(self.speed * math.sqrt(2) / 2), round(self.speed * math.sqrt(2) / 2))
            self.direction = 2
        elif key[pg.K_w]:
            self.rect.move_ip(0, -self.speed)
            self.direction = 3
        elif key[pg.K_s]:
            self.rect.move_ip(0, self.speed)
            self.direction = 0
        elif key[pg.K_a]:
            self.rect.move_ip(-self.speed, 0)
            self.direction = 1
        elif key[pg.K_d]:
            self.rect.move_ip(self.speed, 0)
            self.direction = 2
    
        self.image = pg.transform.scale(player_sprite_sheet.subsurface((0, 48 * self.direction), (25, 48)), (50, 96))

        if self.direction == 1 or self.direction == 2:
            self.hitbox.width = self.rect.width - 22
        else:
            self.hitbox.width = self.rect.width - 11

        self.rect = self.rect.clamp(self.map.rect)
        self.hitbox.center = self.rect.center
        self.hitbox.bottom = self.rect.bottom - 8

        if key[pg.K_LEFT] and key[pg.K_UP]:
            self.shoot(135)
            self.direction = 1
        elif key[pg.K_LEFT] and key[pg.K_DOWN]:
            self.shoot(225)
            self.direction = 1
        elif key[pg.K_RIGHT] and key[pg.K_UP]:
            self.shoot(45)
            self.direction = 2
        elif key[pg.K_RIGHT] and key[pg.K_DOWN]:
            self.shoot(315)
            self.direction = 2
        elif key[pg.K_LEFT]:
            self.shoot(180)
            self.direction = 1
        elif key[pg.K_RIGHT]:
            self.shoot(0)
            self.direction = 2
        elif key[pg.K_UP]:
            self.shoot(90)
            self.direction = 3
        elif key[pg.K_DOWN]:
            self.shoot(270)
            self.direction = 0

        for powerup in sprites.all_powerups:
            if self.hitbox.colliderect(powerup.hitbox):
                if type(powerup) == Coffee:
                    self.speed = 5.5
                    powerup.kill()

        for enemy in sprites.all_enemies:
            if self.hitbox.colliderect(enemy.hitbox):
                current_hit = pg.time.get_ticks()
                if current_hit - self.last_hit >= self.iframes:
                    self.last_hit = current_hit
                    self.lives -= 1
        
        for enemy_shot in sprites.all_enemy_shots:
            if self.hitbox.colliderect(enemy_shot.hitbox):
                current_hit = pg.time.get_ticks()
                if current_hit - self.last_hit >= self.iframes:
                    self.last_hit = current_hit
                    self.lives -= 1
                    enemy_shot.kill()

        if self.lives == 0:
            self.kill()
    
    def shoot(self, angle):
        current_shot = pg.time.get_ticks()
        if current_shot - self.last_shot >= self.shot_cooldown:
            self.last_shot = current_shot
            shot = Shot(pg.transform.scale(shot_sprite, (36, 14)), self.hitbox.center, 0, 0, self.shot_speed, angle, self.map)
            sprites.all_syringes.add(shot)
            sprites.all_sprites.add(shot)
