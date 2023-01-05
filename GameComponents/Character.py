import pygame
from .Object import Object

class Character(Object):
    CHARACTER_SPEED = 10
    def __init__(self, group, pos, image_name=None):
        super().__init__(group, image_name)
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

class Player(Character):
    mario_image = 'mar.png'
    CHARACTER_SPEED = 10

    def __init__(self, group, pos):
        super().__init__(group, pos, ('Image', self.mario_image))