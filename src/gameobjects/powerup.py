import pygame as pg, os, paths

powerup_sprite = pg.transform.scale(pg.image.load(os.path.join(paths.powerups_folder, 'powerup.png')), (24, 24)).convert_alpha()
coffee_sprite = pg.transform.scale(pg.image.load(os.path.join(paths.powerups_folder, 'coffee.png')), (24, 24)).convert_alpha()
mask_sprite = pg.transform.scale(pg.image.load(os.path.join(paths.powerups_folder, 'mask.png')), (24, 16)).convert_alpha()


class Powerup(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = powerup_sprite
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width / 2
        self.rect.y = y - self.rect.height / 2
        self.hitbox = self.rect


class Coffee(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = coffee_sprite
        self.duration = 5000


class Mask(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = mask_sprite
        self.duration = 5000
