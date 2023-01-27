import pygame
from .Object import Object

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

class Character(Object):
    G = -0.25
    Vx, Vy = 4, 0
    event = None

    def __init__(self, group, pos, image_name=None, form='rect'):
        super().__init__(group, image_name, size=[50, 50], take_size=True, colorkey=-1, form=form)
        self.rect.left, self.rect.top = pos

class Cube(Character):
    cube_image = 'cube.png'

    def __init__(self, group, pos):
        super().__init__(group, pos, ('Color', 'yellow'))

    def get_event(self, events, window):
        for key, value in events.items():
            if key in (pygame.K_UP, pygame.K_SPACE)  and value:
                if pygame.sprite.spritecollideany(self, window.platforms):
                    self.jump()
        self.move(window)

    def jump(self):
        self.Vy -= 7

    def move(self, window):
        self.rect = self.rect.move(0, -1)
        self.falling(window)
        self.running(window)
        self.rect = self.rect.move(0, 1)

    def falling(self, window):
        dir, mod = sign(self.Vy), int(abs(self.Vy))
        for i in range(mod):
            self.rect = self.rect.move(0, dir)
            if pygame.sprite.spritecollideany(self, window.platforms):
                self.rect = self.rect.move(0, -dir)
                self.Vy = 0
                return 0
        self.Vy -= self.G

    def running(self, window):
        dir, mod = sign(self.Vx), int(abs(self.Vx))
        for i in range(mod):
            self.rect = self.rect.move(dir, 0)
            if pygame.sprite.spritecollideany(self, window.platforms):
                self.rect = self.rect.move(-dir, 0)
                self.event = 'restart'

class Ufo(Character):
    ufo_image = 'ufo.png'
    hold = False

    def __init__(self, group, pos):
        super().__init__(group, pos, ('Color', 'black'))

    def get_event(self, events, window):
        for key, value in events.items():
            if key in (pygame.K_UP, pygame.K_SPACE) and value and not self.hold:
                self.jump()
                self.hold = True
            if key in (pygame.K_UP, pygame.K_SPACE) and not value:
                self.hold = False
        self.move(window)

    def jump(self):
        self.Vy = -5

    def move(self, window):
        self.rect = self.rect.move(0, -1)
        self.falling(window)
        self.running(window)
        self.rect = self.rect.move(0, 1)

    def falling(self, window):
        dir, mod = sign(self.Vy), int(abs(self.Vy))
        for i in range(mod):
            self.rect = self.rect.move(0, dir)
            if pygame.sprite.spritecollideany(self, window.platforms):
                self.rect = self.rect.move(0, -dir)
                self.Vy = 0
                return 0
        self.Vy -= self.G

    def running(self, window):
        dir, mod = sign(self.Vx), int(abs(self.Vx))
        for i in range(mod):
            self.rect = self.rect.move(dir, 0)
            if pygame.sprite.spritecollideany(self, window.platforms):
                self.rect = self.rect.move(-dir, 0)
                self.event = 'restart'

class Ball(Character):
    ball_image = 'ball.png'
    G = -0.4

    def __init__(self, group, pos):
        super().__init__(group, pos, ('Color', 'red'), form='circle')

    def get_event(self, events, window):
        for key, value in events.items():
            if key in (pygame.K_UP, pygame.K_SPACE) and value:
                if pygame.sprite.spritecollideany(self, window.platforms):
                    self.jump()
        self.move(window)

    def jump(self):
        self.G *= -1
        self.rect = self.rect.move(0, -sign(self.G) * 2)

    def move(self, window):
        self.rect = self.rect.move(0, sign(self.G))
        self.falling(window)
        self.running(window)
        self.rect = self.rect.move(0, -sign(self.G))

    def falling(self, window):
        dir, mod = sign(self.Vy), int(abs(self.Vy))
        for i in range(mod):
            self.rect = self.rect.move(0, dir)
            if pygame.sprite.spritecollideany(self, window.platforms):
                self.rect = self.rect.move(0, -dir)
                self.Vy = 0
                return 0
        self.Vy -= self.G

    def running(self, window):
        dir, mod = sign(self.Vx), int(abs(self.Vx))
        for i in range(mod):
            self.rect = self.rect.move(dir, 0)
            if pygame.sprite.spritecollideany(self, window.platforms):
                self.rect = self.rect.move(-dir, 0)
                self.event = 'restart'

class Ship(Character):
    ship_image = 'ship.png'

    def __init__(self, group, pos):
        super().__init__(group, pos, ('Color', 'black'))

    def get_event(self, events, window):
        for key, value in events.items():
            if key in (pygame.K_UP, pygame.K_SPACE)  and value:
                self.jump()
        self.move(window)

    def jump(self):
        self.Vy -= 0.6

    def move(self, window):
        self.rect = self.rect.move(0, -1)
        self.falling(window)
        self.running(window)
        self.rect = self.rect.move(0, 1)

    def falling(self, window):
        dir, mod = sign(self.Vy), int(abs(self.Vy))
        for i in range(mod):
            self.rect = self.rect.move(0, dir)
            if pygame.sprite.spritecollideany(self, window.platforms):
                self.rect = self.rect.move(0, -dir)
                self.Vy = 0
                return 0
        self.Vy -= self.G

    def running(self, window):
        dir, mod = sign(self.Vx), int(abs(self.Vx))
        for i in range(mod):
            self.rect = self.rect.move(dir, 0)
            if pygame.sprite.spritecollideany(self, window.platforms):
                self.rect = self.rect.move(-dir, 0)
                self.event = 'restart'