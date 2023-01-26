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
    Vx, Vy = 5, 0

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

    def jump(self):
        self.Vy -= 7

    def falling(self, window):
        dir, mod = sign(self.Vy), int(abs(self.Vy))
        for i in range(mod):
            self.rect = self.rect.move(0, dir)
            if pygame.sprite.spritecollideany(self, window.platforms):
                self.rect = self.rect.move(0, -dir)
                self.Vy = 0
                return 0
        else:
            self.Vy -= self.G

    def running(self, window):
        dir, mod = sign(self.Vx), int(abs(self.Vx))
        for i in range(mod):
            self.rect = self.rect.move(dir, 0)
            if pygame.sprite.spritecollideany(self, window.platforms):
                self.rect = self.rect.move(-dir, 0)
                self.Vx = 0
            self.rect = self.rect.move(0, 1)
            if not pygame.sprite.spritecollideany(self, window.platforms):
                if self.Vx < 5:
                    self.Vx += 1
            self.rect = self.rect.move(0, -1)

class Cube(Character):
    mario_image = 'cube.png'

    def __init__(self, group, pos):
        super().__init__(group, pos, ('Image', self.mario_image))

    def get_event(self, events, window):
        for key, value in events.items():
            if key == pygame.K_UP and value:
                if pygame.sprite.spritecollideany(self, window.platforms):
                    self.jump()
        self.update(window)