import pygame as pg, math
from gameobjects.map import Map


class Shot(pg.sprite.Sprite):
    def __init__(self, image, center, xdisplacement, ydisplacement, speed, angle, map: Map):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.rotate(image, angle)
        self.rect = self.image.get_rect()
        self.hitbox = self.rect
        self.rect.center = center
        self.rect.x += xdisplacement
        self.rect.y += ydisplacement
        self.speed = speed
        self.rads = math.radians(angle)
        self.map = map
    
    def update(self):
        self.rect.move_ip(self.speed * math.cos(self.rads), self.speed * -math.sin(self.rads))
        self.hitbox = self.rect
        
        if not self.map.rect.contains(self.hitbox):
            self.kill()
