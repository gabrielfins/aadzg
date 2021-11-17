import pygame as pg, os, paths

full_heart_sprite = pg.transform.scale(pg.image.load(os.path.join(paths.player_folder, 'heart.png')), (26, 24)).convert_alpha()
empty_heart_sprite = pg.transform.scale(pg.image.load(os.path.join(paths.player_folder, 'empty-heart.png')), (26, 24)).convert_alpha()


class Life(pg.sprite.Sprite):
    def __init__(self, x, y, type = 'full'):
        pg.sprite.Sprite.__init__(self)
        self.image = empty_heart_sprite if type == 'empty' else full_heart_sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
