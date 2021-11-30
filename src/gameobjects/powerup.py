import pygame as pg, os, paths

powerup_sprite = pg.transform.scale(pg.image.load(os.path.join(paths.powerups_folder, 'powerup.png')), (24, 24)).convert_alpha()
coffee_sprite = pg.transform.scale(pg.image.load(os.path.join(paths.powerups_folder, 'coffee.png')), (24, 24)).convert_alpha()
mask_sprite = pg.transform.scale(pg.image.load(os.path.join(paths.powerups_folder, 'mask.png')), (24, 16)).convert_alpha()
heart_sprite = pg.transform.scale(pg.image.load(os.path.join(paths.player_folder, 'heart.png')), (26, 24)).convert_alpha()
frame_sprite = pg.transform.scale(pg.image.load(os.path.join(paths.powerups_folder, 'frame.png')), (40, 40)).convert_alpha()
multishot_sprite = pg.transform.scale(pg.image.load(os.path.join(paths.powerups_folder, 'multishot.png')), (30, 30)).convert_alpha()
fast_shot_sprite = pg.transform.scale(pg.image.load(os.path.join(paths.powerups_folder, 'fast_shot.png')), (30, 30)).convert_alpha()

class Coffee(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = coffee_sprite
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width / 2
        self.rect.y = y - self.rect.height / 2
        self.duration = 5000
        self.hitbox = self.rect
        self.tick = pg.time.get_ticks()

    def update(self):
        current_tick = pg.time.get_ticks()
        if current_tick - self.tick >= 10000:
            self.kill()


class FakeCoffee(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = coffee_sprite
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width / 2
        self.rect.y = y - self.rect.height / 2
        self.hitbox = self.rect


class Mask(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = mask_sprite
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width / 2
        self.rect.y = y - self.rect.height / 2
        self.duration = 5000
        self.hitbox = self.rect
        self.tick = pg.time.get_ticks()

    def update(self):
        current_tick = pg.time.get_ticks()
        if current_tick - self.tick >= 10000:
            self.kill()


class FakeMask(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = mask_sprite
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width / 2
        self.rect.y = y - self.rect.height / 2
        self.hitbox = self.rect


class Heart(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = heart_sprite
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width / 2
        self.rect.y = y - self.rect.height / 2
        self.duration = 0
        self.hitbox = self.rect
        self.tick = pg.time.get_ticks()

    def update(self):
        current_tick = pg.time.get_ticks()
        if current_tick - self.tick >= 10000:
            self.kill()


class Frame(pg.sprite.Sprite):
    def __init__(self, x, y) -> None:
        pg.sprite.Sprite.__init__(self)
        self.image = frame_sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - self.rect.height


class MultiShot(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = multishot_sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.duration = 5000
        self.hitbox = self.rect
        self.tick = pg.time.get_ticks()

    def update(self):
        current_tick = pg.time.get_ticks()
        if current_tick - self.tick >= 10000:
            self.kill()


class FakeMultiShot(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = multishot_sprite
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width / 2
        self.rect.y = y - self.rect.height / 2
        self.hitbox = self.rect


class FastShot(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = fast_shot_sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.duration = 5000
        self.hitbox = self.rect
        self.tick = pg.time.get_ticks()

    def update(self):
        current_tick = pg.time.get_ticks()
        if current_tick - self.tick >= 10000:
            self.kill()


class FakeFastShot(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = fast_shot_sprite
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width / 2
        self.rect.y = y - self.rect.height / 2
        self.hitbox = self.rect
