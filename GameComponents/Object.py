import pygame
from .Imageloading import load_image

class Object(pygame.sprite.Sprite):
    def __init__(self, group, image_name):
        super().__init__(group)
        self.image = load_image(image_name)
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

class Stair(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group[0])
        self.add(group[1])
        self.image = pygame.Surface([10, 50])
        pygame.draw.rect(self.image, pygame.Color("red"), (0, 0, 10, 50))
        self.rect = pygame.Rect(pos[0], pos[1], 10, 50)