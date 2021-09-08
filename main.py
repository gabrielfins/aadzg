import pygame as pg, globals, sprites, colors, tests

pg.init()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            elif event.key == pg.K_F1:
                sprites.show_hitboxes = not sprites.show_hitboxes
            elif event.key == pg.K_F2:
                sprites.show_image_boxes = not sprites.show_image_boxes
                
    globals.screen.fill(colors.BLACK)

    sprites.all_sprites.update()
    sprites.camera.update(sprites.player)

    for sprite in sprites.all_sprites:
        globals.screen.blit(sprite.image, sprites.camera.apply(sprite))
        
    tests.draw_image_boxes()
    tests.draw_hitboxes()

    pg.display.update()
    globals.clock.tick(globals.FPS)

pg.quit()
