import pygame, os, paths
from player import Player
from obstacle import Obstacle

pygame.init()

(WIDTH, HEIGHT) = (900, 600)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('As Aventuras do Zé Gotinha')

background_sprite = pygame.transform.scale(pygame.image.load(os.path.join(paths.sprites_folder, 'background.png')), (WIDTH, HEIGHT)).convert()

all_sprites = pygame.sprite.Group()
all_obstacles = pygame.sprite.Group()

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

    all_sprites.update()
    screen.blit(background_sprite, (0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
