import pygame
from .Object import Object

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

class Character(Object):
    G = -0.2
    Ng = 0.8
    Ns = 0.9
    Vx = 0
    Vy = 0
    Vmax = 10

    def __init__(self, group, pos, image_name=None):
        super().__init__(group, image_name)
        self.rect.top = pos[1]
        self.rect.left = pos[0]

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
        d = sign(self.Vy)
        self.rect = self.rect.move(0, int(abs(self.Vy)) * d)
        if pygame.sprite.spritecollideany(self, window.stairs):
            self.Vy = 0
        elif abs(self.Vy) > self.Vmax:
            self.Vy = self.Vmax * d
        else:
            self.Vy -= self.G
        while pygame.sprite.spritecollideany(self, window.platforms):
            self.rect = self.rect.move(0, -d)
            self.Vy = 0

    def running(self, window):
        d = sign(self.Vx)
        self.rect = self.rect.move(int(abs(self.Vx)) * d, 0)
        if pygame.sprite.spritecollideany(self, window.stairs):
            self.Vx = 0
        elif abs(self.Vx) > self.Vmax:
            self.Vx = self.Vmax * d
        self.rect = self.rect.move(0, 1)
        if pygame.sprite.spritecollideany(self, window.platforms):
            self.Vx = self.Vx * self.Ng
        else:
            self.Vx = self.Vx * self.Ns
        self.rect = self.rect.move(0, -1)
        while pygame.sprite.spritecollideany(self, window.platforms):
            self.rect = self.rect.move(-d, 0)
            self.Vx = 0

class Player(Character):
    mario_image = 'mar.png'

    def __init__(self, group, pos):
        super().__init__(group, pos, ('Image', self.mario_image))