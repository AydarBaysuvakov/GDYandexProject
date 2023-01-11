import pygame
from .LoadComponents import load_image

class Object(pygame.sprite.Sprite):
    def __init__(self, group, image_name=None, size=[10, 10], take_size=False):
        super().__init__(group)
        if image_name is None:
            self.image = pygame.Surface(size)
            self.image.fill(pygame.color.Color('white'))
        elif image_name[0] == 'Image':
            self.image = load_image(image_name[1])
            if take_size:
                self.image = pygame.transform.scale(self.image, size)
        elif image_name[0] == 'Animation':
            self.image = load_image(image_name[1])
        elif image_name[0] == 'Color':
            self.image = pygame.Surface(size)
            self.image.fill(pygame.color.Color(image_name[1]))
        self.rect = self.image.get_rect()
        if take_size:
            self.rect.w = size[0]
            self.rect.h = size[1]

    def update(self):
        pass