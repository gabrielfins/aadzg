import pygame as pg, globals, sprites, colors, testing

pg.init()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            elif event.key == pg.K_F2:
                sprites.show_image_boxes = not sprites.show_image_boxes
            elif event.key == pg.K_F3:
                sprites.show_hitboxes = not sprites.show_hitboxes

    globals.screen.fill(colors.BLACK)

    sprites.all_sprites.update()
    sprites.camera.update(sprites.player)
    
    sprites.all_sprites.draw(globals.screen)
    testing.draw()

    pg.display.update()
    globals.clock.tick(globals.FPS)

pg.quit()
