import pygame as pg, os, paths, math, sprites
from gameobjects.map import Map
from gameobjects.shot import Shot
from gameobjects.powerup import Mask, Powerup, Coffee

player_sprite_sheet = pg.image.load(os.path.join(paths.player_folder, 'player.png')).convert_alpha()
shot_sprite = pg.image.load(os.path.join(paths.player_folder, 'syringe.png')).convert_alpha()

all_lives = pg.sprite.Group()


class Player(pg.sprite.Sprite):
    def __init__(self, map: Map):
        pg.sprite.Sprite.__init__(self)
        self.animation_sprites = []
        for i in range(4):
            sprites = []
            for j in range(4):
                img = pg.transform.scale(player_sprite_sheet.subsurface((25 * i, 48 * j), (25, 48)), (50, 96))
                sprites.append(img)
            self.animation_sprites.append(sprites)
            
        self.animation_step = 0
        self.direction = 0
        self.image = pg.transform.scale(player_sprite_sheet.subsurface((0, 48 * self.direction), (25, 48)), (50, 96))
        self.rect = self.image.get_rect()
        self.rect.x = map.rect.width / 2 - self.rect.width / 2
        self.rect.y = map.rect.height / 2 - self.rect.height / 2
        self.hitbox = pg.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height - 64)
        self.map = map
        self.original_speed = 4
        self.speed = self.original_speed
        self.shot_speed = 8
        self.shot_cooldown = 450
        self.last_shot = pg.time.get_ticks()
        self.lives = 3
        self.iframes = 2500
        self.last_hit = pg.time.get_ticks()
        self.powerup_duration = 0
        self.powerup_speed = 0
        self.last_powerup_tick = 0
        self.is_dead = False
        self.is_invincible = False
        

    def update(self):
        self.image = self.animation_sprites[int(self.animation_step if self.animation_step <= 3 else 3)][self.direction]

        key = pg.key.get_pressed()
        self.move(key)
        self.shoot(key)
        self.collide_with_entities()
        self.tick_powerup()

        if self.lives == 0:
            self.is_dead = True

    def move(self, key):
        dx = 0
        dy = 0
        is_moving = False

        if key[pg.K_w] or key[pg.K_s] and key[pg.K_a] or key[pg.K_d]:
            self.speed = round(self.original_speed * math.sqrt(2) / 2) + self.powerup_speed
        else:
            self.speed = self.original_speed + self.powerup_speed

        if key[pg.K_w] or key[pg.K_s] or key[pg.K_a] or key[pg.K_d]:
            if self.animation_step == 0:
                self.animation_step = 1
            if self.animation_step >= 4:
                self.animation_step = 0
            self.animation_step += .08
        else:
            self.animation_step = 0


        if key[pg.K_w]:
            dy = -self.speed
            self.direction = 3
        if key[pg.K_s]:
            dy = self.speed
            self.direction = 0
        if key[pg.K_a]:
            dx = -self.speed
            self.direction = 1
        if key[pg.K_d]:
            dx = self.speed
            self.direction = 2

        self.rect.move_ip(dx, 0)

        block_hit_list = pg.sprite.spritecollide(self, sprites.all_obstacles, False)
        for block in block_hit_list:
            if dx > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.move_ip(0, dy)

        block_hit_list = pg.sprite.spritecollide(self, sprites.all_obstacles, False)
        for block in block_hit_list:
            if dy > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        if self.direction == 1 or self.direction == 2:
            self.hitbox.width = self.rect.width - 30
        else:
            self.hitbox.width = self.rect.width - 20

        self.rect = self.rect.clamp(self.map.rect)
        self.hitbox.center = self.rect.center
        self.hitbox.bottom = self.rect.bottom - 8
    
    def shoot(self, key):
        angle = 0
        shoot = True
        if key[pg.K_LEFT] and key[pg.K_UP]:
            angle = 135
            self.direction = 1
        elif key[pg.K_LEFT] and key[pg.K_DOWN]:
            angle = 225
            self.direction = 1
        elif key[pg.K_RIGHT] and key[pg.K_UP]:
            angle = 45
            self.direction = 2
        elif key[pg.K_RIGHT] and key[pg.K_DOWN]:
            angle = 315
            self.direction = 2
        elif key[pg.K_LEFT]:
            angle = 180
            self.direction = 1
        elif key[pg.K_RIGHT]:
            angle = 0
            self.direction = 2
        elif key[pg.K_UP]:
            angle = 90
            self.direction = 3
        elif key[pg.K_DOWN]:
            angle = 270
            self.direction = 0
        else:
            shoot = False
        
        if shoot:
            current_shot = pg.time.get_ticks()
            if current_shot - self.last_shot >= self.shot_cooldown:
                self.last_shot = current_shot
                shot = Shot(pg.transform.scale(shot_sprite, (36, 14)), self.hitbox.center, 0, 0, self.shot_speed, angle, self.map)
                sprites.all_syringes.add(shot)
                sprites.all_sprites.add(shot)

    def collide_with_entities(self):
        for powerup in sprites.all_powerups:
            if self.hitbox.colliderect(powerup.hitbox):
                if type(powerup) == Powerup:
                    self.reset_powerups()
                    powerup.kill()
                elif type(powerup) == Coffee:
                    self.reset_powerups()
                    self.powerup_speed = 2
                    self.set_active_powerup(powerup)
                elif type(powerup) == Mask:
                    self.reset_powerups()
                    self.is_invincible = True
                    self.set_active_powerup(powerup)

        if not self.is_invincible:
            for enemy in sprites.all_enemies:
                if self.hitbox.colliderect(enemy.hitbox):
                    self.get_hit()


            for enemy_shot in sprites.all_enemy_shots:
                if self.hitbox.colliderect(enemy_shot.hitbox):
                    if self.get_hit():
                        enemy_shot.kill()

    def reset_powerups(self):
        self.powerup_speed = 0
        self.is_invincible = False

    def tick_powerup(self):
        current_powerup_tick = pg.time.get_ticks()
        if current_powerup_tick - self.last_powerup_tick >= self.powerup_duration:
            self.powerup_duration = 0
            self.reset_powerups()

    def set_active_powerup(self, powerup: Powerup):
        self.powerup_duration = powerup.duration
        self.last_powerup_tick = pg.time.get_ticks()
        powerup.kill()

    def get_hit(self):
        current_hit = pg.time.get_ticks()
        is_hit = current_hit - self.last_hit >= self.iframes
        if is_hit:
            self.last_hit = current_hit
            self.lives -= 1
        
        return is_hit
