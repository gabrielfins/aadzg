import pygame as pg, os, paths, sprites
from shot import Shot
from random import randrange

enemy_sprite_sheet = pg.image.load(os.path.join(paths.images_folder, 'bicho1.png'))
enemy_sprite_sheet2 = pg.image.load(os.path.join(paths.images_folder, 'bicho2.png'))


class SeekingEnemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_sprite_sheet.convert_alpha()
        self.imgs_corredor = []
        for i in range(7):
            img = enemy_sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pg.transform.scale(img, (32 * 3, 32 * 3))
            self.imgs_corredor.append(img)

        self.index_lista = 0
        self.image = self.imgs_corredor[self.index_lista]
        self.rect = self.image.get_rect()
        self.hitbox = pg.Rect(0, 0, 17 * 3, 17 * 3)
        self.hitbox.center = self.rect.center
        self.mask = pg.mask.from_surface(self.image)
        self.rect.y = randrange(170, 310, 62)
        self.rect.x = randrange(-100, 200, 60)

    def update(self):
        if self.index_lista > 6:
            self.index_lista = 0

        self.index_lista += 0.22
        self.image = self.imgs_corredor[int(self.index_lista)]

        if self.rect.x > sprites.map.rect.width:
            self.rect.x = -100
            self.rect.y = randrange(170, 310, 62)

        self.rect.x += 1
        self.hitbox.center = self.rect.center

        for syringe in sprites.all_syringes:
            if self.hitbox.colliderect(syringe):
                self.kill()
                syringe.kill()


class ShootingEnemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_sprite_sheet2.convert_alpha()
        self.imgs_cuspidor = []
        for i in range(16):
            img = enemy_sprite_sheet2.subsurface((i * 32, 0), (32, 32))
            img = pg.transform.scale(img, (32 * 3, 32 * 3))
            self.imgs_cuspidor.append(img)

        self.shot_image = pg.transform.scale(pg.image.load(os.path.join(paths.images_folder, 'enemy-shot.png')), (24, 24)).convert_alpha()
        self.index_lista = 0
        self.image = self.imgs_cuspidor[self.index_lista]
        self.rect = self.image.get_rect()
        self.hitbox = pg.Rect(0, 0, 17 * 3, 23 * 3)
        self.mask = pg.mask.from_surface(self.image)
        self.rect.y = 70
        self.rect.x = 80
        self.shot_speed = 5
        self.shot_cooldown = 1000
        self.last_shot = pg.time.get_ticks()

    def update(self):
        if self.index_lista > 15:
            self.index_lista = 0
        
        self.index_lista += 0.18
        self.image = self.imgs_cuspidor[int(self.index_lista)]
        
        if self.index_lista >= 11:
            self.shoot(self.shot_speed, 1, 0)

        self.hitbox.center = self.rect.center

        for syringe in sprites.all_syringes:
            if self.hitbox.colliderect(syringe):
                self.kill()
                syringe.kill()

    def shoot(self, shot_speed, horizontal_velocity, vertical_velocity):
        current_shot = pg.time.get_ticks()
        if current_shot - self.last_shot >= self.shot_cooldown:
            self.last_shot = current_shot
            shot = Shot(self.shot_image, self.rect.x + self.rect.width - 30, self.rect.y + 30, shot_speed, horizontal_velocity, vertical_velocity, 0)
            sprites.all_enemy_shots.add(shot)
            sprites.all_sprites.add(shot)
