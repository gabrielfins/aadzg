import pygame as pg, colors
from gameobjects.text import Text


class Button(pg.sprite.Sprite):
    def __init__(self, text, text_size, color, hover_color, x, y, width, height, horizontal_align = 'left', vertical_align = 'top', border_radius = 0):
        pg.sprite.Sprite.__init__(self)
        self.text = text
        self.button_text = Text(self.text, text_size, colors.WHITE, 0, 0)
        self.original_color = color
        self.hover_color = hover_color
        self.color = self.original_color
        self.image = pg.Surface((width, height))
        self.border_radius = border_radius
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.mouse_hover = self.rect.collidepoint(pg.mouse.get_pos())
        self.horizontal_align = horizontal_align
        self.vertical_align = vertical_align

    def update(self):
        self.set_rounded()
        if self.horizontal_align == 'right':
            self.rect.x = self.x - self.rect.width
        elif self.horizontal_align == 'center':
            self.rect.x = self.x - self.rect.width / 2
        else:
            self.rect.x = self.x

        if self.horizontal_align == 'bottom':
            self.rect.y = self.y - self.rect.height
        elif self.horizontal_align == 'center':
            self.rect.y = self.y - self.rect.height / 2
        else:
            self.rect.y = self.y

        self.button_text.x = self.rect.x + self.rect.width / 2 - self.button_text.rect.width / 2
        self.button_text.y = self.rect.y + self.rect.height / 2 - self.button_text.rect.height / 2
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.color = self.hover_color
        else:
            self.color = self.original_color

    def set_rounded(self):
        self.image.fill(self.color)
        size = self.image.get_size()
        self.rect_image = pg.Surface(size, pg.constants.SRCALPHA)
        self.rect = pg.draw.rect(self.rect_image, (255, 255, 255), (0, 0, *size), border_radius = int(self.border_radius))
        self.image = self.image.copy().convert_alpha()
        self.image.blit(self.rect_image, (0, 0), None, pg.BLEND_RGBA_MIN)
