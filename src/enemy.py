import pygame, os
from random import randrange

dir_principal = os.path.dirname(__file__)
dir_imgs = os.path.join(dir_principal, 'sprites')
enemy_sprite_sheet = pygame.image.load(os.path.join(dir_imgs, 'bicho1.png'))
enemy_sprite_sheet2 = pygame.image.load(os.path.join(dir_imgs, 'bicho2.png'))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_sprite_sheet.convert_alpha()
        self.imgs_corredor = []
        for i in range(7):
            img = enemy_sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))
            self.imgs_corredor.append(img)

        self.index_lista = 0
        self.image = self.imgs_corredor[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
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

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_sprite_sheet2.convert_alpha()
        self.imgs_cuspidor = []
        for i in range(16):
            img = enemy_sprite_sheet2.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))
            self.imgs_cuspidor.append(img)

        self.index_lista = 0
        self.image = self.imgs_cuspidor[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = 70
        self.rect.x = 80


    def update(self):
        if self.index_lista > 15:
            self.index_lista = 0
        self.index_lista += 0.18
        self.image = self.imgs_cuspidor[int(self.index_lista)]