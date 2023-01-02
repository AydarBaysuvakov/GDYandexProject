import pygame
from .Object import Object

class Character(Object):
    CHARACTER_SPEED = 10
    def __init__(self, group, pos):
        super().__init__(group, 'mar.pnj')
        self.rect.top = pos[1]
        self.rect.left = pos[0]

    def update(self):
        pass

    def walk(self, direction):
        self.rect = self.rect.move(direction * self.CHARACTER_SPEED, 0)

    def jump(self):
        pass