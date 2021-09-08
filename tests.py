import pygame as pg, globals, sprites, colors


def draw_image_boxes():
    if sprites.show_image_boxes:
        pg.draw.rect(globals.screen, colors.CYAN, sprites.camera.apply(sprites.player), 1)

        for syringe in sprites.all_syringes:
            pg.draw.rect(globals.screen, colors.RED, sprites.camera.apply(syringe), 1)

        for enemy in sprites.all_enemies:
            pg.draw.rect(globals.screen, colors.CYAN, sprites.camera.apply(enemy), 1)

        for powerup in sprites.all_powerups:
            pg.draw.rect(globals.screen, colors.CYAN, sprites.camera.apply(powerup), 1)

def draw_hitboxes():
    if sprites.show_hitboxes:
        pg.draw.rect(globals.screen, colors.RED, sprites.camera.apply_rect(sprites.player.hitbox), 1)

        for syringe in sprites.all_syringes:
            pg.draw.rect(globals.screen, colors.RED, sprites.camera.apply(syringe), 1)

        for enemy in sprites.all_enemies:
            pg.draw.rect(globals.screen, colors.RED, sprites.camera.apply(enemy), 1)

        for powerup in sprites.all_powerups:
            pg.draw.rect(globals.screen, colors.RED, sprites.camera.apply(powerup), 1)

