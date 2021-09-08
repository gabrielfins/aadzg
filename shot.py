import pygame as pg, sprites


class Shot(pg.sprite.Sprite):
    def __init__(self, image, center, speed, horizontal_velocity, vertical_velocity, angle):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.rotate(image, angle)
        self.rect = self.image.get_rect()
        self.hitbox = self.rect
        self.rect.center = center
        self.speed = speed
        self.horizontal_velocity = horizontal_velocity
        self.vertical_velocity = vertical_velocity
    
    def update(self):
        self.rect.move_ip(self.speed * self.horizontal_velocity, self.speed * self.vertical_velocity)
        self.hitbox = self.rect
        
        if (self.rect.x + self.rect.width < 0 or
            self.rect.x > sprites.map.rect.width or
            self.rect.y + self.rect.height < 0 or
            self.rect.y > sprites.map.rect.height):
            self.kill()
