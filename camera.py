import pygame as pg


class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.last_x = 0
        self.last_y = 0

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(self.width / 4)
        y = -target.rect.y + int(self.height / 4)
        
        x = min(0, x)
        x = max(-(self.width - self.width / 2), x)
        y = min(0, y)
        y = max(-(self.height - self.height / 2), y)

        self.camera = pg.Rect(x, y, self.width, self.height)
