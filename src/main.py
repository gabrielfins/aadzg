import pygame as pg, globals, sprites, colors, screens.menu, screens.controls, os, paths
from gameobjects.button import Button
from pygame import mixer

pg.init()
all_sprites = pg.sprite.Group()
all_buttons = sprites.ButtonGroup()

mixer.init()
mixer.music.load(os.path.join(paths.resources_folder, 'Tema_fundo.mp3'))
mixer.music.set_volume(0.2)
mixer.music.play(-1)

interface = pg.transform.scale(pg.image.load(os.path.join(paths.images_folder, 'interface.png')), (globals.WIDTH, globals.HEIGHT)).convert_alpha()

play_button = Button('Jogar', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 2, 376, 150, 40, 'center', 'center')
play_button.border_radius = play_button.rect.height / 2
all_buttons.add(play_button)

controls_button = Button('Controles', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 2, 436, 150, 40, 'center', 'center')
controls_button.border_radius = play_button.rect.height / 2
all_buttons.add(controls_button)

exit_button = Button('Sair', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 2, globals.HEIGHT - 50, 150, 40, 'center', 'center')
exit_button.border_radius = exit_button.rect.height / 2
all_buttons.add(exit_button)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                if play_button.rect.collidepoint(pg.mouse.get_pos()):
                    screens.menu.world_select()
                elif controls_button.rect.collidepoint(pg.mouse.get_pos()):
                    screens.controls.controls()
                elif exit_button.rect.collidepoint(pg.mouse.get_pos()):
                    running = False

    globals.screen.blit(interface, (0, 0))

    all_sprites.update()
    all_buttons.update()
    all_sprites.draw(globals.screen)
    all_buttons.draw(globals.screen)

    pg.display.update()
    globals.clock.tick(globals.FPS)

pg.quit()
