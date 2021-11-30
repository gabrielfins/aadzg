import pygame as pg, globals, sprites, colors, sys
from gameobjects.text import Text
from gameobjects.button import Button

def game_win():
    all_sprites = pg.sprite.Group()
    all_buttons = sprites.ButtonGroup()

    background = pg.Surface((globals.WIDTH, globals.HEIGHT), pg.SRCALPHA)
    background.fill((0, 0, 0, 200))
    globals.screen.blit(background, (0, 0))

    title = Text('Você venceu!', 48, colors.WHITE, globals.screen_rect.width / 2, 100, 'center', 'center')
    all_sprites.add(title)

    score_text = Text(f'Pontuação Final: {sprites.saved}', 32, colors.WHITE, globals.screen_rect.width / 2, 200, 'center', 'center')
    all_sprites.add(score_text)
    
    exit_button = Button('Sair', 24, colors.DARKBLUE, colors.CYANBLUE, globals.screen_rect.width / 2, globals.screen_rect.height - 50, 150, 40, 'center', 'center')
    exit_button.border_radius = exit_button.rect.height / 2
    all_buttons.add(exit_button)
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    if exit_button.rect.collidepoint(pg.mouse.get_pos()):
                        running = False

        all_sprites.update()
        all_buttons.update()
        all_sprites.draw(globals.screen)
        all_buttons.draw(globals.screen)

        pg.display.update()
        globals.clock.tick(globals.FPS)
