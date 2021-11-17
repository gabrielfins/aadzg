import pygame as pg


class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.rect = pg.Rect(x * 2, y * 2, width * 2, height * 2)
        self.hitbox = self.rect
