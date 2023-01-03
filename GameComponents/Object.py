import pygame
from .Imageloading import load_image

class Object(pygame.sprite.Sprite):
    def __init__(self, group, image_name):
        super().__init__(group)
        self.image = load_image(image_name)
        print(self.image.get_size())
        self.rect = self.image.get_rect()

    def update(self):
        pass

class Platform(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group[0])
        self.add(group[1])
        self.image = pygame.Surface([50, 10])
        pygame.draw.rect(self.image, pygame.Color("white"), (0, 0, 50, 10))
        self.rect = pygame.Rect(pos[0], pos[1], 50, 10)

class Stair(Object):
    def __init__(self, group, pos):
        super().__init__(group[0])
        self.add(group[1])
        self.image = pygame.transform.scale(load_image('ladderMid1.png'), (20, 50))
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
    def __init__(self, group, pos):
        super().__init__(group[0], 'ladderMid1.png')
        self.add(group[1])
        self.image = pygame.transform.scale(self.image, (20, 50))
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]

class Box(Object):
    def __init__(self, group, pos):
        super().__init__(group[0], 'box.png')
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]