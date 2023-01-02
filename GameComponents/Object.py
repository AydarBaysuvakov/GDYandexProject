import pygame
from .Imageloading import load_image

class Object(pygame.sprite.Sprite):
    def __init__(self, group, image_name):
        super().__init__(group)
        self.image = load_image(image_name)
        self.rect = self.image.get_rect()

    def update(self):
        pass