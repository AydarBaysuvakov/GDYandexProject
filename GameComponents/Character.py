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
    hold = False

    def __init__(self, group, pos, window, image_name=None, form='rect'):
        super().__init__(group, image_name, size=[50, 50], take_size=True, colorkey=-1, form=form)
        self.rect.left, self.rect.top = pos
        self.window = window

    def get_event(self, events):
        for key, value in events.items():
            if key in (pygame.K_UP, pygame.K_SPACE, 1) and value:
                if not pygame.sprite.spritecollideany(self, self.window.orbs):
                    self.jump()
                elif not self.hold:
                    for orb in self.window.orbs:
                        if pygame.sprite.collide_circle(self, orb):
                            orb.action(self)
                            self.move()
                self.hold = True
            if key in (pygame.K_UP, pygame.K_SPACE, 1) and not value:
                self.hold = False
        self.move()

    def move(self):
        self.rect = self.rect.move(0, sign(self.G))
        self.falling()
        self.running()
        self.rect = self.rect.move(0, -sign(self.G))

    def falling(self):
        dir, mod = sign(self.Vy), int(abs(self.Vy))
        for i in range(mod):
            self.rect = self.rect.move(0, dir)
            if pygame.sprite.spritecollideany(self, self.window.platforms):
                self.rect = self.rect.move(0, -dir)
                self.Vy = 0
                return 0
        self.Vy -= self.G

    def running(self):
        dir, mod = sign(self.Vx), int(abs(self.Vx))
        for i in range(mod):
            self.rect = self.rect.move(dir, 0)
            if pygame.sprite.spritecollideany(self, self.window.platforms):
                self.rect = self.rect.move(-dir, 0)
                self.event = 'restart'

class Cube(Character):
    cube_image = 'cube.png'

    def __init__(self, group, pos, window):
        super().__init__(group, pos, window,('Color', 'yellow'))

    def jump(self):
        if pygame.sprite.spritecollideany(self, self.window.platforms):
            self.Vy = 7 * sign(self.G)

class Ufo(Character):
    ufo_image = 'ufo.png'

    def __init__(self, group, pos, window):
        super().__init__(group, pos, window, ('Color', 'black'))

    def jump(self):
        if not self.hold:
            self.Vy = 7 * sign(self.G)

class Ball(Character):
    ball_image = 'ball.png'
    G = -0.4

    def __init__(self, group, pos, window):
        super().__init__(group, pos, window, ('Color', 'red'), form='circle')

    def jump(self):
        if pygame.sprite.spritecollideany(self, self.window.platforms):
            self.G *= -1
            self.rect = self.rect.move(0, -sign(self.G) * 2)

class Ship(Character):
    ship_image = 'ship.png'

    def __init__(self, group, pos, window):
        super().__init__(group, pos, window, ('Color', 'black'))

    def jump(self):
        self.Vy -= 0.5