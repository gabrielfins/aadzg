import pygame as pg, os, paths
from map import Map
from camera import Camera
from player import Player
from powerup import Powerup
from enemy import SeekingEnemy, ShootingEnemy, FlyingEnemy


class YAwareGroup(pg.sprite.Group):
    def by_y(self, spr):
        return spr.hitbox.y

    def draw(self, surface):
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sorted(sprites, key=self.by_y):
            self.spritedict[spr] = surface_blit(spr.image, camera.apply_rect(spr.rect))
        self.lostsprites = []

show_hitboxes = False
show_image_boxes = False

powerup_sprite = pg.transform.scale(pg.image.load(os.path.join(paths.images_folder, 'coffee.png')), (24, 24)).convert_alpha()

all_sprites = YAwareGroup()
all_syringes = pg.sprite.Group()
all_powerups = pg.sprite.Group()
all_enemies = pg.sprite.Group()
all_enemy_shots = pg.sprite.Group()

map = Map()
all_sprites.add(map)

camera = Camera(map.rect.width, map.rect.height)

player = Player()
all_sprites.add(player)

powerup = Powerup(powerup_sprite, 300, 300)
all_powerups.add(powerup)
all_sprites.add(powerup)

cuspidor = ShootingEnemy()
all_enemies.add(cuspidor)
all_sprites.add(cuspidor)

for i in range(15):
    baiacu = FlyingEnemy()
    all_enemies.add(baiacu)
    all_sprites.add(baiacu)

for i in range(15):
    corredor = SeekingEnemy()
    all_enemies.add(corredor)
    all_sprites.add(corredor)

all_collidable_groups = [player, all_syringes, all_powerups, all_enemies, all_enemy_shots]
