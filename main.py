import pygame
import colors
import os
from character import Character
from recharge import Recharge
from text import Text

game_folder = os.path.dirname(__file__)
sprites_folder = os.path.join(game_folder, 'sprites')

background_sprite = pygame.transform.scale(
                        pygame.image.load(os.path.join(sprites_folder, 'background.png')), (850, 600))

pygame.init()

(width, height) = (850, 600)
screen = pygame.display.set_mode((width, height))
screen_rect = screen.get_rect()
font = pygame.font.Font(None, 32)

pygame.display.set_caption('The Game: Shooter')

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

recharge = Recharge(screen)
all_sprites.add(recharge)

player = Character(screen, screen_rect.width, screen_rect.height, all_sprites)
all_sprites.add(player)

doses_text = Text(screen, f'{player.doses}', 32, colors.BLACK, player)
all_sprites.add(doses_text)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    key = pygame.key.get_pressed()

    if key[pygame.K_RIGHT] and key[pygame.K_UP]:
        player.shoot('right up')
    if key[pygame.K_RIGHT] and key[pygame.K_DOWN]:
        player.shoot('right down')
    if key[pygame.K_LEFT] and key[pygame.K_UP]:
        player.shoot('left up')
    if key[pygame.K_LEFT] and key[pygame.K_DOWN]:
        player.shoot('left down')
    if key[pygame.K_RIGHT]:
        player.shoot('right')
    if key[pygame.K_LEFT]:
        player.shoot('left')
    if key[pygame.K_UP]:
        player.shoot('up')
    if key[pygame.K_DOWN]:
        player.shoot('down')

    all_sprites.update()

    if player.rect.colliderect(recharge.rect):
        if player.doses < 25:
            player.doses = 25

    screen.blit(background_sprite.convert(), (0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
