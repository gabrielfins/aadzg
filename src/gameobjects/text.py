import pygame as pg, os, paths

pg.font.init()


class Text(pg.sprite.Sprite):
    def __init__(self, text, size, color, x, y, horizontal_align = 'left', vertical_align = 'top'):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.Font(os.path.join(paths.fonts_folder, 'Pixellari.ttf'), size)
        self.text = text
        self.color = color
        self.text_surface = self.font.render(self.text, 1, self.color)
        self.image = self.text_surface
        self.rect = self.image.get_rect()
        self.hitbox = self.rect
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.horizontal_align = horizontal_align
        self.vertical_align = vertical_align

    def update(self):
        self.text_surface = self.font.render(self.text, 1, self.color)
        self.image = self.text_surface
        self.rect = self.image.get_rect()

        if self.horizontal_align == 'right':
            self.rect.x = self.x - self.rect.width
        elif self.horizontal_align == 'center':
            self.rect.x = self.x - self.rect.width / 2
        else:
            self.rect.x = self.x

        if self.vertical_align == 'bottom':
            self.rect.y = self.y - self.rect.height
        elif self.vertical_align == 'center':
            self.rect.y = self.y - self.rect.height / 2
        else:
            self.rect.y = self.y
        