import pygame as pg, globals, sprites, colors

def draw():
    if sprites.show_image_boxes:
        for collidable_object in sprites.all_collidable_groups:
            if type(collidable_object) == pg.sprite.Group:
                for collidable_objects in collidable_object:
                    pg.draw.rect(globals.screen, colors.CYAN, sprites.camera.apply(collidable_objects), 1)
            else:
                pg.draw.rect(globals.screen, colors.CYAN, sprites.camera.apply(collidable_object), 1)

    if sprites.show_hitboxes:
        for collidable_object in sprites.all_collidable_groups:
            if type(collidable_object) == pg.sprite.Group:
                for collidable_objects in collidable_object:
                    pg.draw.rect(globals.screen, colors.RED, sprites.camera.apply_rect(collidable_objects.hitbox), 1)
            else:
                pg.draw.rect(globals.screen, colors.RED, sprites.camera.apply_rect(collidable_object.hitbox), 1)
