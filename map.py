import pygame as pg, globals, os, paths

class Map(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load(os.path.join(paths.images_folder, 'background.png')), (globals.screen_rect.width * 2, globals.screen_rect.height * 2)).convert()
        self.rect = self.image.get_rect()