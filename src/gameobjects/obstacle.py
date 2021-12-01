import pygame as pg, os, paths

trash_rocket_image = pg.image.load(os.path.join(paths.images_folder, 'trash-rocket.png')).convert_alpha()


class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.rect = pg.Rect(x * 2, y * 2, width * 2, height * 2)
        self.hitbox = self.rect


class ObstacleImage(pg.sprite.Sprite):
    def __init__(self, image, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class TrashRocket(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = trash_rocket_image
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width
        self.rect.y = y - self.rect.height
        self.hitbox = self.rect