import pygame as pg, globals, sprites, colors, sys
from gameobjects.text import Text
from gameobjects.button import Button

def pause():
    all_sprites = pg.sprite.Group()
    all_buttons = sprites.ButtonGroup()

    title = Text('Pause', 48, colors.WHITE, globals.screen_rect.width / 2, 100, 'center', 'center')
    all_sprites.add(title)
    
    resume_button = Button('Resumir', 24, colors.BLUE, globals.screen_rect.width / 2, 300, 150, 40, 'center', 'center')
    resume_button.border_radius = resume_button.rect.height / 2
    all_buttons.add(resume_button)

    exit_button = Button('Sair', 24, colors.BLUE, globals.screen_rect.width / 2, globals.screen_rect.height - 100, 150, 40, 'center', 'center')
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
                    if resume_button.rect.collidepoint(pg.mouse.get_pos()):
                        running = False
                        return True
                    elif exit_button.rect.collidepoint(pg.mouse.get_pos()):
                        running = False
                        return False

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
