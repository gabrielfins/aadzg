import pygame as pg, globals, sprites, colors, screens.menu
import pygame.image

from gameobjects.text import Text
from gameobjects.button import Button

pg.init()
interface = pygame.image.load("resources/images/INTERFACE 2.0.png")
bg = pygame.transform.scale(interface, (896, 608))


all_sprites = pg.sprite.Group()
all_buttons = sprites.ButtonGroup()

play_button = Button('Jogar', 24, colors.DARKBLUE, globals.screen_rect.width / 2, 376, 150, 40, 'center', 'center')
play_button.border_radius = play_button.rect.height / 2
all_buttons.add(play_button)

exit_button = Button('Sair', 24, colors.BLUE, globals.screen_rect.width / 2, globals.screen_rect.height - 100, 150, 40, 'center', 'center')
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