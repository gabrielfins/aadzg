import pygame as pg, os, paths
from map import Map
from camera import Camera
from player import Player
from powerup import Powerup
from enemy import Enemy, Enemy2

powerup_sprite = pg.transform.scale(pg.image.load(os.path.join(paths.images_folder, 'coffee.png')), (24, 24)).convert_alpha()

all_sprites = pg.sprite.Group()
all_syringes = pg.sprite.Group()
all_powerups = pg.sprite.Group()
all_enemies = pg.sprite.Group()

map = Map()
all_sprites.add(map)

camera = Camera(map.rect.width, map.rect.height)

cuspidor = Enemy2()
all_enemies.add(cuspidor)
all_sprites.add(cuspidor)

for i in range(10):
    corredor = Enemy()
    all_enemies.add(corredor)
    all_sprites.add(corredor)

powerup = Powerup(powerup_sprite, 300, 300)
all_powerups.add(powerup)
all_sprites.add(powerup)

player = Player()
all_sprites.add(player)

show_hitboxes = False
show_image_boxes = False