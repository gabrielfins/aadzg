import pygame as pg, globals, sprites, colors, sys, os, paths
from gameobjects.text import Text
from gameobjects.button import Button
from gameobjects.obstacle import ObstacleImage

walk_keys_sprite = pg.image.load(os.path.join(paths.images_folder, 'walk_keys.png')).convert_alpha()
shoot_keys_sprite = pg.image.load(os.path.join(paths.images_folder, 'shoot_keys.png')).convert_alpha()

def controls():
    all_sprites = pg.sprite.Group()
    all_buttons = sprites.ButtonGroup()

    title = Text('Controles', 48, colors.WHITE, globals.WIDTH / 2, 100, 'center', 'center')
    all_sprites.add(title)

    walk_image = ObstacleImage(pg.transform.scale(walk_keys_sprite, (192, 128)), globals.WIDTH / 3, 300)
    all_sprites.add(walk_image)

    walk_text = Text('Andar', 32, colors.WHITE, globals.WIDTH / 3, 410, 'center', 'center')
    all_sprites.add(walk_text)

    shoot_image = ObstacleImage(pg.transform.scale(shoot_keys_sprite, (192, 128)), globals.WIDTH / 1.5, 300)
    all_sprites.add(shoot_image)

    shoot_text = Text('Atirar', 32, colors.WHITE, globals.WIDTH / 1.5, 410, 'center', 'center')
    all_sprites.add(shoot_text)
    
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
                    if back_button.rect.collidepoint(pg.mouse.get_pos()):
                        running = False

        globals.screen.fill(colors.BLACK)

        all_sprites.update()
        all_buttons.update()
        all_sprites.draw(globals.screen)
        all_buttons.draw(globals.screen)

        pg.display.update()
        globals.clock.tick(globals.FPS)
