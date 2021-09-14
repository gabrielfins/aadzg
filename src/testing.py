import pygame as pg, globals, sprites, colors
from gameobjects.camera import Camera

def draw(collidable_groups, camera: Camera):
    if sprites.show_image_boxes:
        for collidable_object in collidable_groups:
            if type(collidable_object) == pg.sprite.Group:
                for collidable_objects in collidable_object:
                    pg.draw.rect(globals.screen, colors.CYAN, camera.apply(collidable_objects), 1)
            else:
                pg.draw.rect(globals.screen, colors.CYAN, camera.apply(collidable_object), 1)

    if sprites.show_hitboxes:
        for collidable_object in collidable_groups:
            if type(collidable_object) == pg.sprite.Group:
                for collidable_objects in collidable_object:
                    pg.draw.rect(globals.screen, colors.RED, camera.apply_rect(collidable_objects.hitbox), 1)
            else:
                pg.draw.rect(globals.screen, colors.RED, camera.apply_rect(collidable_object.hitbox), 1)
