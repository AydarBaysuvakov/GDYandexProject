import pygame
from .LoadComponents import load_image

class Object(pygame.sprite.Sprite):
    def __init__(self, group, image_name=None, size=(10, 10), take_size=False, colorkey=None, form='rect', reverse=False):
        super().__init__(group)
        self.loading_original_image(image_name, size, colorkey, form, take_size)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        if take_size:
            self.rect.w = size[0]
            self.rect.h = size[1]
        if reverse:
            self.image = pygame.transform.rotate(self.image, 180)
        self.mask = pygame.mask.from_surface(self.image)

    def loading_original_image(self, image_name, size, colorkey, form, take_size):
        if image_name is None:
            self.image_orig = pygame.Surface(size)
            self.image_orig.fill(pygame.color.Color('white'))
        elif image_name[0] == 'Image':
            self.image_orig = load_image(image_name[1], colorkey=colorkey)
            if take_size:
                self.image_orig = pygame.transform.scale(self.image_orig, size)
        elif image_name[0] == 'Color':
            self.image_orig = pygame.Surface(size)
            if form == 'circle':
                pygame.draw.circle(self.image_orig, pygame.Color(image_name[1]),
                                   (size[0] // 2, size[1] // 2), size[0] // 2)
                self.image_orig.set_colorkey(pygame.color.Color('black'))
            else:
                self.image_orig.fill(pygame.color.Color(image_name[1]))

class Platform(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group[0])
        self.add(group[1])
        self.image = pygame.Surface([50, 10])
        pygame.draw.rect(self.image, pygame.Color("white"), (0, 0, 50, 10))
        self.rect = pygame.Rect(pos[0], pos[1], 50, 10)

class Box(Object):
    def __init__(self, group, pos):
        super().__init__(group[0], ('Image', 'block.jpg'), size=[40, 40], take_size=True)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]

class Ground(Object):
    def __init__(self, group, pos=(-500, 0), size=(2000, 500)):
        super().__init__(group[0], ('Image', 'floor.jpg'), size, take_size=True)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]

class WinZone(Object):
    def __init__(self, group, pos=(1500, -1000), size=(500, 1500)):
        super().__init__(group[0], ('Image', 'floor.jpg'), size, take_size=True)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]

class Spike(Object):
    def __init__(self, group, pos):
        super().__init__(group[0], ('Image', 'spike.png'), size=[40, 40], take_size=True)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]

class ReverseSpike(Object):
    def __init__(self, group, pos):
        super().__init__(group[0], ('Image', 'reversespike.png'), size=[40, 40], take_size=True)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]

class Coin(Object):
    def __init__(self, group, pos, collected=True):
        if collected:
            super().__init__(group[0], ('Image', 'coin.png'), size=[40, 40], take_size=True)
        else:
            super().__init__(group[0], ('Color', 'blue'), size=[40, 40], take_size=True, form='circle')
        self.SG = group
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        self.active = False

    def action(self, player):
        if not self.active:
            self.SG[0].remove(self)
            self.SG[1].remove(self)
            player.coin += 1
        self.active = True