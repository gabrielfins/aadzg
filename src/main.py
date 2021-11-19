import pygame as pg, globals, sprites, colors, screens.menu, os, paths
from gameobjects.button import Button

pg.init()
all_sprites = pg.sprite.Group()
all_buttons = sprites.ButtonGroup()

interface = pg.transform.scale(pg.image.load(os.path.join(paths.images_folder, 'interface.png')), (globals.WIDTH, globals.HEIGHT)).convert_alpha()

play_button = Button('Jogar', 24, colors.DARKBLUE, globals.screen_rect.width / 2, 376, 150, 40, 'center', 'center')
play_button.border_radius = play_button.rect.height / 2
all_buttons.add(play_button)

exit_button = Button('Sair', 24, colors.BLUE, globals.screen_rect.width / 2, globals.screen_rect.height - 50, 150, 40, 'center', 'center')
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
                elif exit_button.rect.collidepoint(pg.mouse.get_pos()):
                    running = False

    globals.screen.blit(interface, (0, 0))

    for button in all_buttons:
        if button.rect.collidepoint(pg.mouse.get_pos()):
            button.color = colors.DARKBLUE
        else:
            button.color = colors.CYANBLUE

    all_sprites.update()
    all_buttons.update()
    all_sprites.draw(globals.screen)
    all_buttons.draw(globals.screen)

    pg.display.update()
    globals.clock.tick(globals.FPS)

pg.quit()