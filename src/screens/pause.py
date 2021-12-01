import pygame as pg, globals, sprites, colors, sys
from gameobjects.text import Text
from gameobjects.button import Button

def pause():
    all_sprites = pg.sprite.Group()
    all_buttons = sprites.ButtonGroup()

    background = pg.Surface((globals.WIDTH, globals.HEIGHT), pg.SRCALPHA)
    background.fill((0, 0, 0, 200))
    globals.screen.blit(background, (0, 0))

    title = Text('Pause', 48, colors.WHITE, globals.WIDTH / 2, 100, 'center', 'center')
    all_sprites.add(title)
    
    resume_button = Button('Resumir', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 2, 300, 150, 40, 'center', 'center')
    resume_button.border_radius = resume_button.rect.height / 2
    all_buttons.add(resume_button)

    exit_button = Button('Sair', 24, colors.DARKBLUE, colors.CYANBLUE, globals.WIDTH / 2, globals.HEIGHT - 50, 150, 40, 'center', 'center')
    exit_button.border_radius = exit_button.rect.height / 2
    all_buttons.add(exit_button)
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                    return True
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    if resume_button.rect.collidepoint(pg.mouse.get_pos()):
                        running = False
                        return True
                    elif exit_button.rect.collidepoint(pg.mouse.get_pos()):
                        running = False
                        return False

        all_sprites.update()
        all_buttons.update()
        all_sprites.draw(globals.screen)
        all_buttons.draw(globals.screen)

        pg.display.update()
        globals.clock.tick(globals.FPS)
