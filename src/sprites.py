import pygame as pg
from gameobjects.camera import Camera

show_hitboxes = False
show_image_boxes = False
saved = 0


class YAwareGroup(pg.sprite.Group):
    def by_y(self, spr):
        return spr.hitbox.y

    def draw(self, surface, camera: Camera):
        for spr in sorted(self.sprites(), key=self.by_y):
            self.spritedict[spr] = surface.blit(spr.image, camera.apply_rect(spr.rect))

        self.lostsprites = []

class ButtonGroup(pg.sprite.Group):
    def draw(self, surface):
        for spr in self.sprites():
            self.spritedict[spr] = surface.blit(spr.image, spr.rect)
            self.spritedict[spr] = surface.blit(spr.button_text.image, spr.button_text.rect)

    def update(self):
        for spr in self.sprites():
            spr.update()
            spr.button_text.update()

all_sprites = YAwareGroup()
all_syringes = pg.sprite.Group()
all_enemies = pg.sprite.Group()
all_enemy_shots = pg.sprite.Group()
all_powerups = pg.sprite.Group()
all_obstacles = pg.sprite.Group()
all_fixed_sprites = pg.sprite.Group()
all_fixed_powerups = pg.sprite.Group()
