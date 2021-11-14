from random import random, randrange
import pygame as pg, globals, colors, sprites, testing, screens.pause, screens.game_over, screens.game_win
from gameobjects.camera import Camera
from gameobjects.map import Map
from gameobjects.player import Player
from gameobjects.enemy import DissipatingEnemy, FlyingEnemy, SeekingEnemy, ShootingEnemy, StumblingEnemy
from gameobjects.text import Text
from gameobjects.obstacle import Obstacle
from gameobjects.life import Life
from gameobjects.powerup import Frame

def level(map_path):
    map = Map(map_path)
    sprites.all_sprites.add(map)

    for tile_object in map.tmxdata.objects:
        if tile_object.name == 'obstacle':
            obstacle = Obstacle(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            sprites.all_obstacles.add(obstacle)

    camera = Camera(map.rect.width, map.rect.height)

    player = Player(map)
    sprites.all_sprites.add(player)

    powerup_frame = Frame(10, globals.HEIGHT - 50)
    sprites.all_fixed_sprites.add(powerup_frame)

    all_collidable_groups = [player,
                             sprites.all_syringes,
                             sprites.all_enemies,
                             sprites.all_enemy_shots,
                             sprites.all_powerups,
                             sprites.all_obstacles]

    all_lives = []

    for i in range(player.lives):
        empty_life = Life(30 * i + 10, 10, 'empty')
        sprites.all_fixed_sprites.add(empty_life)
        life = Life(30 * i + 10, 10)
        all_lives.append(life)
        sprites.all_fixed_sprites.add(life)

    saved_text = Text(f'Salvos: {sprites.saved}', 32, colors.WHITE, globals.screen_rect.width - 20, 20, 'right')
    sprites.all_fixed_sprites.add(saved_text)

    wave = 0
    wave_indicator = 0
    spawned_enemies = 0
    clock = pg.time.Clock()
    dt = 0
    timer = 11000

    wave_text = Text(f'Rodada {wave_indicator}', 32, colors.WHITE, globals.screen_rect.width / 2, 20, 'center')
    sprites.all_fixed_sprites.add(wave_text)

    time_to_wave_text = Text(f'{int(timer / 1000 if timer >= 0 else 0)}', 24, colors.WHITE, globals.screen_rect.width / 2, 50, 'center')
    sprites.all_fixed_sprites.add(time_to_wave_text)

    wave_tick = pg.time.get_ticks()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = screens.pause.pause()
                    if running == False:
                        empty_sprite_groups()
                elif event.key == pg.K_F2:
                    sprites.show_image_boxes = not sprites.show_image_boxes
                elif event.key == pg.K_F3:
                    sprites.show_hitboxes = not sprites.show_hitboxes

        sprites.all_sprites.update()
        saved_text.text = f'Salvos: {sprites.saved}'
        wave_text.text = f'Rodada {wave_indicator}'
        time_to_wave_text.text = f'{int(timer / 1000 if timer >= 0 else 0)}'
        sprites.all_fixed_sprites.update()
        camera.update(player)

        for life in all_lives:
            sprites.all_fixed_sprites.remove(life)

        all_lives.clear()
        for i in range(player.lives):
            life = Life(30 * i + 10, 10)
            all_lives.append(life)
            sprites.all_fixed_sprites.add(life)

        timer -= dt
        if timer <= 0:
            wave_indicator = wave + 1 if wave != 5 else wave
            if wave == 0:
                for i in range(0, 6, 1):
                    current_time = pg.time.get_ticks()
                    if current_time - wave_tick >= 500:
                        wave_tick = current_time
                        create_enemy(SeekingEnemy, player, map, camera)
                        spawned_enemies += 1
                if spawned_enemies >= 20:
                    wave += 1
                    spawned_enemies = 0
                    timer = 16000
            if wave == 1:
                for i in range(0, 9, 1):
                    current_time = pg.time.get_ticks()
                    if current_time - wave_tick >= 550:
                        type = randrange(0, 2, 1)
                        if type == 0:
                            create_enemy(SeekingEnemy, player, map, camera)
                        elif type == 1:
                            create_enemy(ShootingEnemy, player, map, camera)

                        wave_tick = current_time
                        spawned_enemies += 1
                if spawned_enemies >= 35:
                    wave += 1
                    spawned_enemies = 0
                    timer = 16000
            if wave == 2:
                for i in range(0, 11, 1):
                    current_time = pg.time.get_ticks()
                    if current_time - wave_tick >= 600:
                        type = randrange(0, 3, 1)
                        if type == 0:
                            create_enemy(SeekingEnemy, player, map, camera)
                        elif type == 1:
                            create_enemy(ShootingEnemy, player, map, camera)
                        elif type == 2:
                            create_enemy(FlyingEnemy, player, map, camera)
                        wave_tick = current_time
                        spawned_enemies += 1
                if spawned_enemies >= 35:
                    wave += 1
                    spawned_enemies = 0
                    timer = 21000
            if wave == 3:
                for i in range(0, 13, 1):
                    current_time = pg.time.get_ticks()
                    if current_time - wave_tick >= 625:
                        type = randrange(0, 4, 1)
                        if type == 0:
                            create_enemy(SeekingEnemy, player, map, camera)
                        elif type == 1:
                            create_enemy(ShootingEnemy, player, map, camera)
                        elif type == 2:
                            create_enemy(FlyingEnemy, player, map, camera)
                        elif type == 3:
                            create_enemy(DissipatingEnemy, player, map, camera)
                        wave_tick = current_time
                        spawned_enemies += 1
                if spawned_enemies >= 40:
                    wave += 1
                    spawned_enemies = 0
                    timer = 21000
            if wave == 4:
                for i in range(0, 15, 1):
                    current_time = pg.time.get_ticks()
                    if current_time - wave_tick >= 650:
                        type = randrange(0, 5, 1)
                        if type == 0:
                            create_enemy(SeekingEnemy, player, map, camera)
                        elif type == 1:
                            create_enemy(ShootingEnemy, player, map, camera)
                        elif type == 2:
                            create_enemy(FlyingEnemy, player, map, camera)
                        elif type == 3:
                            create_enemy(DissipatingEnemy, player, map, camera)
                        elif type == 4:
                            create_enemy(StumblingEnemy, player, map, camera)
                        wave_tick = current_time
                        spawned_enemies += 1
                if spawned_enemies >= 40:
                    wave += 1
                    spawned_enemies = 0


        dt = clock.tick(60)

        sprites.all_sprites.draw(globals.screen, camera)
        sprites.all_fixed_sprites.draw(globals.screen)
        sprites.all_fixed_powerups.draw(globals.screen)
        testing.draw(all_collidable_groups, camera)

        if player.is_dead:
            screens.game_over.game_over()
            empty_sprite_groups()
            running = False

        if wave >= 5 and len(sprites.all_enemies) == 0 and spawned_enemies == 0:
            screens.game_win.game_win()
            empty_sprite_groups()
            running = False

        pg.display.update()
        globals.clock.tick(globals.FPS)

def create_enemy(enemy_type, player, map, camera):
    location = randrange(0, 4, 1)
    x = 0
    y = 0

    if location == 0:
        x = map.rect.width / 2
        y = 0
    elif location == 1:
        x = 0
        y = map.rect.height / 2
    elif location == 2:
        x = map.rect.width
        y = map.rect.height / 2
    else:
        x = map.rect.width / 2
        y = map.rect.height

    if enemy_type == SeekingEnemy or enemy_type == FlyingEnemy or enemy_type == StumblingEnemy:
        enemy = enemy_type(player, x, y)
    elif enemy_type == ShootingEnemy or enemy_type == DissipatingEnemy:
        enemy = enemy_type(player, map, camera, x, y)

    sprites.all_enemies.add(enemy)
    sprites.all_sprites.add(enemy)

def empty_sprite_groups():
    sprites.all_sprites.empty()
    sprites.all_enemies.empty()
    sprites.all_enemy_shots.empty()
    sprites.all_powerups.empty()
    sprites.all_syringes.empty()
    sprites.all_obstacles.empty()
    sprites.all_fixed_sprites.empty()
    sprites.saved = 0