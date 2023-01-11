import pygame
from .Object import Object

class Platform(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group[0])
        self.add(group[1])
        self.image = pygame.Surface([50, 10])
        pygame.draw.rect(self.image, pygame.Color("white"), (0, 0, 50, 10))
        self.rect = pygame.Rect(pos[0], pos[1], 50, 10)

class Stair(Object):
    def __init__(self, group, pos):
        super().__init__(group[0], ('Image', 'ladderMid1.png'))
        self.add(group[1])
        self.image = pygame.transform.scale(self.image, (20, 50))
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]

class Box(Object):
    def __init__(self, group, pos):
        super().__init__(group[0], ('Image', 'box.png'))
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]

class Ground(Object):
    def __init__(self, group, pos, size):
        super().__init__(group[0], ('Image', 'grassMid.png'), size, take_size=True)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]

class Wall(Object):
    def __init__(self, group, pos, size):
        super().__init__(group[0], ('Image', 'sandCenter.png'), size, take_size=True)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]