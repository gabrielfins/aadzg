import pygame, os, paths

pygame.font.init()

pixellari = os.path.join(paths.fonts_folder, 'Pixellari.ttf')
font_xs = pygame.font.Font(pixellari, 16)
font_s = pygame.font.Font(pixellari, 24)
font_m = pygame.font.Font(pixellari, 32)
font_l = pygame.font.Font(pixellari, 40)
font_xl = pygame.font.Font(pixellari, 48)
