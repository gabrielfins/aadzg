import pygame, os, paths
from player import Player
from obstacle import Obstacle
from enemy import Enemy, Enemy2

pygame.init()

(WIDTH, HEIGHT) = (900, 600)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('As Aventuras do Zé Gotinha')

background_sprite = pygame.transform.scale(pygame.image.load(os.path.join(paths.sprites_folder, 'background.png')), (WIDTH, HEIGHT)).convert()

all_sprites = pygame.sprite.Group()
all_obstacles = pygame.sprite.Group()
grupo_obstaculos = pygame.sprite.Group()

cuspidor = Enemy2()
all_sprites.add(cuspidor)
grupo_obstaculos.add(cuspidor)

for i in range(10):
    corredor = Enemy()
    all_sprites.add(corredor)
    grupo_obstaculos.add(corredor)

obstacle = Obstacle(screen, 50, 100)
all_obstacles.add(obstacle)

for obstacle in all_obstacles:
    all_sprites.add(obstacle)

player = Player(screen, all_sprites)
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    colisoes = pygame.sprite.spritecollide(player, grupo_obstaculos, False, pygame.sprite.collide_mask)

    screen.blit(background_sprite, (0, 0))
    all_sprites.draw(screen)

    if colisoes:
        pass
    else:
        all_sprites.update()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
