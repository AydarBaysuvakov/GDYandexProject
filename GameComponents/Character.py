import json
import pygame
from .Object import Object

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

class Character(Object):
    G = -0.225
    Vx, Vy = 4, 0
    JUMP_FORCE = 6
    event = None
    hold = False
    coin = 0

    def __init__(self, group, pos, window, image_name=None, form='rect'):
        super().__init__(group, image_name, size=[40, 40], take_size=True, colorkey=pygame.color.Color('white'), form=form)
        self.rect.left, self.rect.top = pos
        self.window = window

    def get_event(self, events):
        for key, value in events.items():
            if key in (pygame.K_UP, pygame.K_SPACE, 1) and value:
                if not pygame.sprite.spritecollideany(self, self.window.orbs):
                    self.jump()
                for orb in self.window.orbs:
                    if pygame.sprite.collide_circle(self, orb):
                        orb.action(self)
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
            for spike in self.window.spikes:
                if pygame.sprite.collide_mask(self, spike):
                    self.rect = self.rect.move(0, -dir)
                    self.event = 'restart'
            if pygame.sprite.spritecollideany(self, self.window.platforms):
                self.rect = self.rect.move(0, -dir)
                self.Vy = 0
                return 0
        self.Vy -= self.G

    def running(self):
        dir, mod = sign(self.Vx), int(abs(self.Vx))
        for i in range(mod):
            self.rect = self.rect.move(dir, 0)
            if pygame.sprite.collide_mask(self, self.window.winzone):
                self.event = 'win'
            elif pygame.sprite.spritecollideany(self, self.window.platforms):
                self.rect = self.rect.move(-dir, 0)
                self.event = 'restart'
            elif pygame.sprite.spritecollideany(self, self.window.spikes):
                self.rect = self.rect.move(-dir, 0)
                self.event = 'restart'
            for portal in self.window.portals:
                if pygame.sprite.collide_rect(self, portal):
                    portal.action(self)

class Cube(Character):
    def __init__(self, group, pos, window):
        self.cube_image = json.load(open('Data/skins.json'))['cubes']['curent']
        super().__init__(group, pos, window,('Image', self.cube_image))

    def jump(self):
        if pygame.sprite.spritecollideany(self, self.window.platforms):
            self.Vy = self.JUMP_FORCE * sign(self.G)

class Ufo(Character):
    def __init__(self, group, pos, window):
        self.ufo_image = json.load(open('Data/skins.json'))['ufos']['curent']
        super().__init__(group, pos, window, ('Color', 'green'))

    def jump(self):
        if not self.hold:
            self.Vy = self.JUMP_FORCE * sign(self.G)

class Ball(Character):
    G = -0.4

    def __init__(self, group, pos, window):
        self.ball_image = json.load(open('Data/skins.json'))['balls']['curent']
        super().__init__(group, pos, window, ('Color', 'red'), form='circle')

    def jump(self):
        if pygame.sprite.spritecollideany(self, self.window.platforms):
            self.G *= -1
            self.rect = self.rect.move(0, -sign(self.G) * 2)

class Ship(Character):
    FLY_VELOCITY = 0.5
    def __init__(self, group, pos, window):
        self.ship_image = json.load(open('Data/skins.json'))['ships']['curent']
        super().__init__(group, pos, window, ('Color', '#FF69B4'))

    def jump(self):
        self.Vy += self.FLY_VELOCITY * sign(self.G)