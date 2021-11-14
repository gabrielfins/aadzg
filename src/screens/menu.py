import pygame as pg, globals, sprites, colors, screens.level, sys, os, paths
from gameobjects.text import Text
from gameobjects.button import Button


def world_select():
    all_sprites = pg.sprite.Group()
    all_buttons = sprites.ButtonGroup()

    title = Text('Seleção de Mundo', 48, colors.WHITE, globals.screen_rect.width / 2, 100, 'center', 'center')
    all_sprites.add(title)
    
    world1_button = Button('Mundo 1', 24, colors.BLUE, globals.screen_rect.width / 3, 300, 150, 40, 'center', 'center')
    world1_button.border_radius = world1_button.rect.height / 2
    all_buttons.add(world1_button)

    world2_button = Button('Mundo 2', 24, colors.BLUE, globals.screen_rect.width / 1.5, 300, 150, 40, 'center', 'center')
    world2_button.border_radius = world2_button.rect.height / 2
    all_buttons.add(world2_button)

    back_button = Button('Voltar', 24, colors.BLUE, globals.screen_rect.width / 2, globals.screen_rect.height - 100, 150, 40, 'center', 'center')
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
                    elif back_button.rect.collidepoint(pg.mouse.get_pos()):
                        running = False

        globals.screen.fill(colors.BLACK)

        for button in all_buttons:
            if button.rect.collidepoint(pg.mouse.get_pos()):
                button.color = colors.MAGENTA
            else:
                button.color = colors.BLUE

        all_sprites.update()
        all_buttons.update()
        all_sprites.draw(globals.screen)
        all_buttons.draw(globals.screen)

        pg.display.update()
        globals.clock.tick(globals.FPS)

def world1_levels_select():
    all_sprites = pg.sprite.Group()
    all_buttons = sprites.ButtonGroup()

    title = Text('Mundo 1', 48, colors.WHITE, globals.screen_rect.width / 2, 100, 'center', 'center')
    all_sprites.add(title)
    
    world1_button = Button('Fase 1', 24, colors.BLUE, globals.screen_rect.width / 3, 300, 150, 40, 'center', 'center')
    world1_button.border_radius = world1_button.rect.height / 2
    all_buttons.add(world1_button)

    world2_button = Button('Fase 2', 24, colors.BLUE, globals.screen_rect.width / 1.5, 300, 150, 40, 'center', 'center')
    world2_button.border_radius = world2_button.rect.height / 2
    all_buttons.add(world2_button)

    back_button = Button('Voltar', 24, colors.BLUE, globals.screen_rect.width / 2, globals.screen_rect.height - 100, 150, 40, 'center', 'center')
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
                        screens.level.level(os.path.join(paths.maps_folder, 'map1.tmx'))
                    elif world2_button.rect.collidepoint(pg.mouse.get_pos()):
                        screens.level.level(os.path.join(paths.maps_folder, 'map2.tmx'))
                    elif back_button.rect.collidepoint(pg.mouse.get_pos()):
                        running = False

        globals.screen.fill(colors.BLACK)

        for button in all_buttons:
            if button.rect.collidepoint(pg.mouse.get_pos()):
                button.color = colors.MAGENTA
            else:
                button.color = colors.BLUE

        all_sprites.update()
        all_buttons.update()
        all_sprites.draw(globals.screen)
        all_buttons.draw(globals.screen)

        pg.display.update()
        globals.clock.tick(globals.FPS)

def world2_levels_select():
    all_sprites = pg.sprite.Group()
    all_buttons = sprites.ButtonGroup()

    title = Text('Mundo 2', 48, colors.WHITE, globals.screen_rect.width / 2, 100, 'center', 'center')
    all_sprites.add(title)
    
    world1_button = Button('Fase 1', 24, colors.BLUE, globals.screen_rect.width / 3, 300, 150, 40, 'center', 'center')
    world1_button.border_radius = world1_button.rect.height / 2
    all_buttons.add(world1_button)

    world2_button = Button('Fase 2', 24, colors.BLUE, globals.screen_rect.width / 1.5, 300, 150, 40, 'center', 'center')
    world2_button.border_radius = world2_button.rect.height / 2
    all_buttons.add(world2_button)

    back_button = Button('Voltar', 24, colors.BLUE, globals.screen_rect.width / 2, globals.screen_rect.height - 100, 150, 40, 'center', 'center')
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
                    if back_button.rect.collidepoint(pg.mouse.get_pos()):
                        running = False

        globals.screen.fill(colors.BLACK)

        for button in all_buttons:
            if button.rect.collidepoint(pg.mouse.get_pos()):
                button.color = colors.MAGENTA
            else:
                button.color = colors.BLUE

        all_sprites.update()
        all_buttons.update()
        all_sprites.draw(globals.screen)
        all_buttons.draw(globals.screen)

        pg.display.update()
        globals.clock.tick(globals.FPS)
