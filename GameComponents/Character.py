import pygame
from .Object import Object

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

class Character(Object):
    G, Ng, Ns = -0.2, 0.8, 0.9
    Vx, Vy = 0, 0
    Vmax = 9

    def __init__(self, group, pos, image_name=None):
        super().__init__(group, image_name, size=[50, 50], take_size=True, colorkey=-1)
        self.rect.left, self.rect.top = pos


    def update(self, window):
        self.rect = self.rect.move(0, -1)
        self.falling(window)
        self.running(window)
        self.rect = self.rect.move(0, 1)

    def walk(self, direction):
        self.Vx += direction

    def up(self, direction):
        self.Vy += direction * 2

    def jump(self):
        self.Vy -= 7

    def falling(self, window):
        dir, mod = sign(self.Vy), int(abs(self.Vy))
        if mod > self.Vmax:
            self.Vy = dir * self.Vmax
            mod = self.Vmax
        for i in range(mod):
            self.rect = self.rect.move(0, dir)
            if pygame.sprite.spritecollideany(self, window.platforms):
                self.rect = self.rect.move(0, -dir)
                self.Vy = 0
                return 0
        if pygame.sprite.spritecollideany(self, window.stairs):
            self.Vy = 0
        else:
            self.Vy -= self.G

    def running(self, window):
        dir, mod = sign(self.Vx), int(abs(self.Vx))
        if mod > self.Vmax:
            self.Vx = dir * self.Vmax
            mod = self.Vmax
        for i in range(mod):
            self.rect = self.rect.move(dir, 0)
            if pygame.sprite.spritecollideany(self, window.platforms):
                self.rect = self.rect.move(-dir, 0)
                self.Vx = 0
                return 0
        self.rect = self.rect.move(0, 1)
        if pygame.sprite.spritecollideany(self, window.platforms) or\
                pygame.sprite.spritecollideany(self, window.stairs):
            self.Vx = self.Vx * self.Ng
        else:
            self.Vx = self.Vx * self.Ns
        self.rect = self.rect.move(0, -1)

class Player(Character):
    mario_image = 'cube.png'

    def __init__(self, group, pos):
        super().__init__(group, pos, ('Image', self.mario_image))

    def get_event(self, events, window):
        for key, value in events.items():
            if pygame.sprite.spritecollideany(self, window.stairs) or \
                    pygame.sprite.spritecollideany(self, window.platforms):
                if key == pygame.K_RIGHT and value:
                    self.walk(1.2)
                if key == pygame.K_LEFT and value:
                    self.walk(-1.2)
            else:
                if key == pygame.K_RIGHT and value:
                    self.walk(0.3)
                if key == pygame.K_LEFT and value:
                    self.walk(-0.3)
            if key == pygame.K_UP and value:
                if pygame.sprite.spritecollideany(self, window.stairs):
                    self.up(-1)
                elif pygame.sprite.spritecollideany(self, window.platforms):
                    self.jump()
            if key == pygame.K_DOWN and value:
                if pygame.sprite.spritecollideany(self, window.stairs):
                    self.up(1)
        self.update(window)