import pygame as pg, os, paths, globals, colors, sprites, testing
from gameobjects.camera import Camera
from gameobjects.map import Map
from gameobjects.player import Player
from gameobjects.enemy import SeekingEnemy, ShootingEnemy, FlyingEnemy, DissipatingEnemy
from gameobjects.text import Text

def level1():    
    map = Map(os.path.join(paths.maps_folder, 'map1.tmx'))
    sprites.all_sprites.add(map)
   
    camera = Camera(map.rect.width, map.rect.height)

    player = Player(map)
    sprites.all_sprites.add(player)

    all_collidable_groups = [player, sprites.all_syringes, sprites.all_enemies, sprites.all_enemy_shots, sprites.all_powerups]

    saved = 0
    text = Text(f'salvos: {saved}', 32, colors.WHITE, globals.screen_rect.width - 20, 20, 'right')
    sprites.all_fixed_sprites.add(text)

    shooter = ShootingEnemy(map)
    sprites.all_enemies.add(shooter)
    sprites.all_sprites.add(shooter)

    dissipater = DissipatingEnemy(map)
    sprites.all_enemies.add(dissipater)
    sprites.all_sprites.add(dissipater)

    for i in range(15):
        pufferfish = FlyingEnemy(map)
        sprites.all_enemies.add(pufferfish)
        sprites.all_sprites.add(pufferfish)

    for i in range(15):
        runner = SeekingEnemy(map)
        sprites.all_enemies.add(runner)
        sprites.all_sprites.add(runner)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                    sprites.all_sprites.empty()
                    sprites.all_enemies.empty()
                    sprites.all_enemy_shots.empty()
                    sprites.all_powerups.empty()
                    sprites.all_syringes.empty()
                    sprites.all_fixed_sprites.empty()
                elif event.key == pg.K_F2:
                    sprites.show_image_boxes = not sprites.show_image_boxes
                elif event.key == pg.K_F3:
                    sprites.show_hitboxes = not sprites.show_hitboxes

        sprites.all_sprites.update()
        sprites.all_fixed_sprites.update()
        camera.update(player)
    
        sprites.all_sprites.draw(globals.screen, camera)
        sprites.all_fixed_sprites.draw(globals.screen)
        testing.draw(all_collidable_groups, camera)

        pg.display.update()
        globals.clock.tick(globals.FPS)
