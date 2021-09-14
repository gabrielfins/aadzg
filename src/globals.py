import pygame as pg, os, paths

FPS = 60
WIDTH = 896
HEIGHT = 608

screen = pg.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()
clock = pg.time.Clock()

pg.display.set_caption('As Aventuras do Zé Gotinha Beta')
pg.display.set_icon(pg.image.load(os.path.join(paths.images_folder, 'icon.png')).convert_alpha())
