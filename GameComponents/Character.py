import pygame
from .Object import Object

class Character(Object):
    CHARACTER_SPEED = 10
    mario_image = 'mar.png'
    def __init__(self, group, pos):
        super().__init__(group, self.mario_image)
        self.rect.top = pos[1]
        self.rect.left = pos[0]

    def update(self, window):
        if not pygame.sprite.spritecollideany(self, window.stairs) and \
                not pygame.sprite.spritecollideany(self, window.platforms):
            self.rect = self.rect.move(0, 1)

    def walk(self, direction):
        self.rect = self.rect.move(self.CHARACTER_SPEED * direction, 0)

    def up(self, direction):
        self.rect = self.rect.move(0, self.CHARACTER_SPEED * direction)

    def jump(self):
        self.rect = self.rect.move(0, -self.CHARACTER_SPEED)