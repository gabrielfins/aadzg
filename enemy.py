import pygame as pg, os, paths, sprites
from random import randrange

enemy_sprite_sheet = pg.image.load(os.path.join(paths.images_folder, 'bicho1.png'))
enemy_sprite_sheet2 = pg.image.load(os.path.join(paths.images_folder, 'bicho2.png'))


class Enemy(pg.sprite.Sprite):
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
        self.mask = pg.mask.from_surface(self.image)
        self.rect.y = randrange(170, 310, 62)
        self.rect.x = randrange(-100, 200, 60)

    def update(self):
        if self.index_lista > 6:
            self.index_lista = 0
        self.index_lista += 0.22
        self.image = self.imgs_corredor[int(self.index_lista)]
        if self.rect.topleft[0] > 900:
            self.rect.x = -100
            self.rect.y = randrange(170, 310, 62)
        self.rect.x += 1
        for syringe in sprites.all_syringes:
            if self.rect.colliderect(syringe):
                self.kill()
                syringe.kill()


class Enemy2(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_sprite_sheet2.convert_alpha()
        self.imgs_cuspidor = []
        for i in range(16):
            img = enemy_sprite_sheet2.subsurface((i * 32, 0), (32, 32))
            img = pg.transform.scale(img, (32 * 3, 32 * 3))
            self.imgs_cuspidor.append(img)

        self.index_lista = 0
        self.image = self.imgs_cuspidor[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.y = 70
        self.rect.x = 80

    def update(self):
        if self.index_lista > 15:
            self.index_lista = 0
        self.index_lista += 0.18
        self.image = self.imgs_cuspidor[int(self.index_lista)]
        for syringe in sprites.all_syringes:
            if self.rect.colliderect(syringe):
                self.kill()
                syringe.kill()
