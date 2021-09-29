import pygame as pg, os, paths, sprites, math
from random import randrange
from gameobjects.player import Player
from gameobjects.map import Map
from gameobjects.shot import Shot

seeking_enemy_sprite_sheet = pg.image.load(os.path.join(paths.enemies_folder, 'seeking-enemy.png')).convert_alpha()
shooting_enemy_sprite_sheet = pg.image.load(os.path.join(paths.enemies_folder, 'shooting-enemy.png')).convert_alpha()
flying_enemy_sprite_sheet = pg.image.load(os.path.join(paths.enemies_folder, 'flying-enemy.png')).convert_alpha()
dissipating_enemy_sprite_sheet = pg.image.load(os.path.join(paths.enemies_folder, 'dissipating-enemy.png')).convert_alpha()
shot_image = pg.transform.scale(pg.image.load(os.path.join(paths.enemies_folder, 'enemy-shot.png')), (24, 24)).convert_alpha()

possible_angles = [0, 45, 90, 135, 180, -45, -90, -135, -180]

class SeekingEnemy(pg.sprite.Sprite):
    def __init__(self, map: Map):
        pg.sprite.Sprite.__init__(self)
        self.image = seeking_enemy_sprite_sheet
        self.imgs_corredor = []
        for i in range(7):
            img = seeking_enemy_sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pg.transform.scale(img, (32 * 3, 32 * 3))
            self.imgs_corredor.append(img)

        self.index_lista = 0
        self.image = self.imgs_corredor[self.index_lista]
        self.rect = self.image.get_rect()
        self.hitbox = pg.Rect(0, 0, 17 * 3, 17 * 3)
        self.hitbox.center = self.rect.center
        self.mask = pg.mask.from_surface(self.image)
        self.rect.y = randrange(500, 650, 62)
        self.rect.x = randrange(-1500, 500, 88)
        self.map = map

    def update(self):
        if self.index_lista > 6:
            self.index_lista = 0

        self.index_lista += 0.22
        self.image = self.imgs_corredor[int(self.index_lista)]

        if self.rect.x > self.map.rect.width:
            self.rect.x = -100
            self.rect.y = randrange(500, 650, 62)

        self.rect.x += 1
        self.hitbox.center = self.rect.center

        for syringe in sprites.all_syringes:
            if self.hitbox.colliderect(syringe):
                self.kill()
                syringe.kill()

class ShootingEnemy(pg.sprite.Sprite):
    def __init__(self, player: Player, map: Map):
        pg.sprite.Sprite.__init__(self)
        self.image = shooting_enemy_sprite_sheet
        self.imgs_cuspidor = []
        for i in range(16):
            img = shooting_enemy_sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pg.transform.scale(img, (32 * 3, 32 * 3))
            self.imgs_cuspidor.append(img)

        self.index_lista = 0
        self.image = self.imgs_cuspidor[self.index_lista]
        self.rect = self.image.get_rect()
        self.hitbox = pg.Rect(0, 0, 17 * 3, 23 * 3)
        self.mask = pg.mask.from_surface(self.image)
        self.rect.y = 300
        self.rect.x = 620
        self.shot_speed = 5
        self.shot_cooldown = 1000
        self.last_shot = pg.time.get_ticks()
        self.player = player
        self.map = map

    def update(self):
        if self.index_lista > 15:
            self.index_lista = 0
        
        self.index_lista += 0.18
        self.image = self.imgs_cuspidor[int(self.index_lista)]
        
        if self.index_lista >= 11:
            x = self.hitbox.centerx + 15
            y = self.hitbox.centery - 20
            dx = self.player.hitbox.centerx - x
            dy = self.player.hitbox.centery - y
            deg = math.degrees(math.atan2(-dy, dx))
            self.shoot(deg)

        self.hitbox.center = self.rect.center

        for syringe in sprites.all_syringes:
            if self.hitbox.colliderect(syringe):
                self.kill()
                syringe.kill()

    def shoot(self, angle):
        current_shot = pg.time.get_ticks()
        if current_shot - self.last_shot >= self.shot_cooldown:
            self.last_shot = current_shot
            shot = Shot(shot_image, self.hitbox.center, 15, -20, self.shot_speed, angle, self.map)
            sprites.all_enemy_shots.add(shot)
            sprites.all_sprites.add(shot)

class FlyingEnemy(pg.sprite.Sprite):
    def __init__(self, map: Map):
        pg.sprite.Sprite.__init__(self)
        self.image = flying_enemy_sprite_sheet
        self.imgs_baiacu = []
        for i in range(63):
            img = flying_enemy_sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pg.transform.scale(img, (32 * 2, 32 * 2))
            self.imgs_baiacu.append(img)

        self.index_lista = 0
        self.image = self.imgs_baiacu[self.index_lista]
        self.rect = self.image.get_rect()
        self.hitbox = pg.Rect(0, 0, 17 * 3, 17 * 3)
        self.hitbox.center = self.rect.center
        self.mask = pg.mask.from_surface(self.image)
        self.rect.y = randrange(-1800, -400, 300)
        self.rect.x = randrange(750, 1000, 80)
        self.map = map

    def update(self):
        if self.index_lista > 62:
            self.index_lista = 0

        self.index_lista += 0.7
        self.image = self.imgs_baiacu[int(self.index_lista)]

        if self.rect.y > self.map.rect.height:
            self.rect.x = randrange(750, 1000, 80)
            self.rect.y = randrange(-1800, -400, 380)

        self.rect.y += 4
        self.hitbox.center = self.rect.center

        for syringe in sprites.all_syringes:
            if self.hitbox.colliderect(syringe):
                self.kill()
                syringe.kill()

class DissipatingEnemy(pg.sprite.Sprite):
    def __init__(self, player: Player, map: Map):
        pg.sprite.Sprite.__init__(self)
        self.image = dissipating_enemy_sprite_sheet
        self.imgs_dissipador = []
        for i in range(80):
            img = dissipating_enemy_sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pg.transform.scale(img, (32 * 4, 32 * 4))
            self.imgs_dissipador.append(img)

        self.index_lista = 0
        self.image = self.imgs_dissipador[self.index_lista]
        self.rect = self.image.get_rect()
        self.hitbox = pg.Rect(0, 0, 23 * 4, 23 * 4)
        self.mask = pg.mask.from_surface(self.image)
        self.rect.y = 900
        self.rect.x = 1200
        self.shot_speed = 5
        self.shot_cooldown = 1000
        self.last_shot = pg.time.get_ticks()
        self.player = player
        self.map = map

    def update(self):
        if self.index_lista > 79:
            self.index_lista = 0

        self.index_lista += 0.7
        self.image = self.imgs_dissipador[int(self.index_lista)]

        if self.index_lista >= 43:
            x = self.hitbox.centerx
            y = self.hitbox.centery
            dx = self.player.hitbox.centerx - x
            dy = self.player.hitbox.centery - y
            deg = math.degrees(math.atan2(-dy, dx))
            self.shoot(deg)

        self.hitbox.center = self.rect.center

        for syringe in sprites.all_syringes:
            if self.hitbox.colliderect(syringe):
                self.kill()
                syringe.kill()

    def shoot(self, angle):
        current_shot = pg.time.get_ticks()
        if current_shot - self.last_shot >= self.shot_cooldown:
            for i in range(-1, 2):
                self.last_shot = current_shot
                shot = Shot(shot_image, self.hitbox.center, 0, 0, self.shot_speed, min((possible_angles), key=lambda i:abs(i-angle)) + i * 20, self.map)
                sprites.all_enemy_shots.add(shot)
                sprites.all_sprites.add(shot)
