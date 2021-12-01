import pygame as pg, globals, sprites, colors, screens.level, sys, os, paths
from gameobjects.text import Text
from gameobjects.button import Button


def world_select():
    all_sprites = pg.sprite.Group()
    all_buttons = sprites.ButtonGroup()

    interface = pg.transform.scale(pg.image.load(os.path.join(paths.images_folder, 'world-select.png')), (globals.WIDTH, globals.HEIGHT)).convert_alpha()
    
    world1_button = Button('Ilha Dos Devorados', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 2, 300, 300, 40, 'center', 'center')
    world1_button.border_radius = world1_button.rect.height / 2
    all_buttons.add(world1_button)

    world2_button = Button('Deserto Dos Infectados', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 2, 360, 300, 40, 'center', 'center')
    world2_button.border_radius = world2_button.rect.height / 2
    all_buttons.add(world2_button)

    world3_button = Button('Bloqueado', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 2, 420, 150, 40, 'center', 'center')
    world3_button.border_radius = world3_button.rect.height / 2
    all_buttons.add(world3_button)

    back_button = Button('Voltar', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 2, globals.HEIGHT - 50, 150, 40, 'center', 'center')
    back_button.border_radius = back_button.rect.height / 2
    all_buttons.add(back_button)
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    if world1_button.rect.collidepoint(pg.mouse.get_pos()):
                        world1_levels_select()
                    elif world2_button.rect.collidepoint(pg.mouse.get_pos()):
                        world2_levels_select()
                    elif world3_button.rect.collidepoint(pg.mouse.get_pos()):
                        world3_levels_select()
                    elif back_button.rect.collidepoint(pg.mouse.get_pos()):
                        running = False

        globals.screen.blit(interface, (0, 0))

        all_sprites.update()
        all_buttons.update()
        all_sprites.draw(globals.screen)
        all_buttons.draw(globals.screen)

        pg.display.update()
        globals.clock.tick(globals.FPS)

def world1_levels_select():
    all_sprites = pg.sprite.Group()
    all_buttons = sprites.ButtonGroup()

    interface = pg.transform.scale(pg.image.load(os.path.join(paths.images_folder, 'ilha-dos-devorados.png')), (globals.WIDTH, globals.HEIGHT)).convert_alpha()

    level1_button = Button('Fase 1', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 5, 360, 150, 40, 'center', 'center')
    level1_button.border_radius = level1_button.rect.height / 2
    all_buttons.add(level1_button)

    level2_button = Button('Fase 2', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 2, 360, 150, 40, 'center', 'center')
    level2_button.border_radius = level2_button.rect.height / 2
    all_buttons.add(level2_button)

    level3_button = Button('Fase 3', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 1.2, 360, 150, 40, 'center', 'center')
    level3_button.border_radius = level3_button.rect.height / 2
    all_buttons.add(level3_button)

    back_button = Button('Voltar', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 2, globals.HEIGHT - 50, 150, 40, 'center', 'center')
    back_button.border_radius = back_button.rect.height / 2
    all_buttons.add(back_button)
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    if level1_button.rect.collidepoint(pg.mouse.get_pos()):
                        screens.level.level(os.path.join(paths.maps_folder, 'world1_level1.tmx'), [20, 24, 28, 32, 36], [1, 1, 1, 2, 2], [400, 450, 500, 550, 600], [11000, 16000, 16000, 16000, 16000], 1)
                    elif level2_button.rect.collidepoint(pg.mouse.get_pos()):
                        screens.level.level(os.path.join(paths.maps_folder, 'world1_level2.tmx'), [24, 28, 32, 36, 40], [1, 1, 2, 2, 3], [450, 500, 550, 575, 600], [11000, 16000, 16000, 16000, 16000])
                    elif level3_button.rect.collidepoint(pg.mouse.get_pos()):
                        screens.level.level(os.path.join(paths.maps_folder, 'world1_level3.tmx'), [28, 32, 36, 40, 44], [1, 2, 2, 3, 4], [500, 540, 580, 620, 660], [11000, 16000, 16000, 16000, 16000])
                    elif back_button.rect.collidepoint(pg.mouse.get_pos()): 
                        running = False

        globals.screen.blit(interface, (0, 0))

        all_sprites.update()
        all_buttons.update()
        all_sprites.draw(globals.screen)
        all_buttons.draw(globals.screen)

        pg.display.update()
        globals.clock.tick(globals.FPS)

def world2_levels_select():
    all_sprites = pg.sprite.Group()
    all_buttons = sprites.ButtonGroup()

    Deserto = pg.transform.scale(pg.image.load(os.path.join(paths.images_folder, 'Deserto_dos_Infectados.png')),(globals.WIDTH, globals.HEIGHT)).convert_alpha()

    level1_button = Button('Fase 1', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 5, 360, 150, 40, 'center', 'center')
    level1_button.border_radius = level1_button.rect.height / 2
    all_buttons.add(level1_button)

    level2_button = Button('Fase 2', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 2, 360, 150, 40, 'center', 'center')
    level2_button.border_radius = level2_button.rect.height / 2
    all_buttons.add(level2_button)

    level3_button = Button('Fase 3', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 1.2, 360, 150, 40, 'center', 'center')
    level3_button.border_radius = level3_button.rect.height / 2
    all_buttons.add(level3_button)

    back_button = Button('Voltar', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 2, globals.HEIGHT - 50, 150, 40, 'center', 'center')
    back_button.border_radius = back_button.rect.height / 2
    all_buttons.add(back_button)
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    if level1_button.rect.collidepoint(pg.mouse.get_pos()):
                        screens.level.level(os.path.join(paths.maps_folder, 'world2_level1.tmx'), [22, 26, 31, 36, 40], [2, 2, 2, 3, 4], [500, 510, 520, 530, 540], [11000, 16000, 16000, 16000, 16000], 0, 4, 3, show_trash_rocket=False)
                    elif level2_button.rect.collidepoint(pg.mouse.get_pos()):
                        screens.level.level(os.path.join(paths.maps_folder, 'world2_level2.tmx'), [26, 29, 34, 40, 46], [2, 2, 3, 4, 4], [500, 525, 550, 575, 600], [11000, 16000, 16000, 16000, 16000])
                    elif level3_button.rect.collidepoint(pg.mouse.get_pos()):
                        screens.level.level(os.path.join(paths.maps_folder, 'world2_level3.tmx'), [29, 36, 40, 43, 48], [2, 2, 3, 4, 5], [510, 540, 570, 600, 630], [11000, 16000, 16000, 16000, 16000], 1)
                    elif back_button.rect.collidepoint(pg.mouse.get_pos()):
                        running = False

        globals.screen.blit(Deserto, (0, 0))

        all_sprites.update()
        all_buttons.update()
        all_sprites.draw(globals.screen)
        all_buttons.draw(globals.screen)

        pg.display.update()
        globals.clock.tick(globals.FPS)

def world3_levels_select():
    all_sprites = pg.sprite.Group()
    all_buttons = sprites.ButtonGroup()

    title = Text('Mundo 3', 48, colors.WHITE, globals.WIDTH / 2, 100, 'center', 'center')
    all_sprites.add(title)
    
    level1_button = Button('Fase 1', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 5, 360, 150, 40, 'center', 'center')
    level1_button.border_radius = level1_button.rect.height / 2
    all_buttons.add(level1_button)

    level2_button = Button('Fase 2', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 2, 360, 150, 40, 'center', 'center')
    level2_button.border_radius = level2_button.rect.height / 2
    all_buttons.add(level2_button)

    level3_button = Button('Fase 3', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 1.2, 360, 150, 40, 'center', 'center')
    level3_button.border_radius = level3_button.rect.height / 2
    all_buttons.add(level3_button)

    back_button = Button('Voltar', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 2, globals.HEIGHT - 50, 150, 40, 'center', 'center')
    back_button.border_radius = back_button.rect.height / 2
    all_buttons.add(back_button)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    if level1_button.rect.collidepoint(pg.mouse.get_pos()):
                        screens.level.level(os.path.join(paths.maps_folder, 'world3_level1.tmx'), [24, 28, 34, 40, 45], [2, 2, 3, 4, 5], [500, 510, 520, 530, 540], [11000, 16000, 16000, 16000, 16000], 1, 3)
                    elif level2_button.rect.collidepoint(pg.mouse.get_pos()):
                        screens.level.level(os.path.join(paths.maps_folder, 'world3_level2.tmx'), [27, 31, 36, 44, 49], [2, 3, 4, 4, 5], [510, 535, 560, 585, 690], [11000, 16000, 16000, 16000, 16000], 1, 4, 2)
                    elif level3_button.rect.collidepoint(pg.mouse.get_pos()):
                        screens.level.level(os.path.join(paths.maps_folder, 'world3_level3.tmx'), [34, 39, 46, 49, 53], [2, 3, 4, 5, 5], [600, 640, 670, 700, 730], [11000, 16000, 16000, 16000, 16000])
                    elif back_button.rect.collidepoint(pg.mouse.get_pos()):
                        running = False

        globals.screen.fill(colors.BLACK)

        all_sprites.update()
        all_buttons.update()
        all_sprites.draw(globals.screen)
        all_buttons.draw(globals.screen)

        pg.display.update()
        globals.clock.tick(globals.FPS)
