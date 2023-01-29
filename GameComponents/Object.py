import pygame
from .LoadComponents import load_image

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

class Object(pygame.sprite.Sprite):
    def __init__(self, group, image_name=None, size=(10, 10), take_size=False, colorkey=None, form='rect'):
        super().__init__(group)
        if image_name is None:
            self.image = pygame.Surface(size)
            self.image.fill(pygame.color.Color('white'))
        elif image_name[0] == 'Image':
            self.image = load_image(image_name[1], colorkey=colorkey)
            if take_size:
                self.image = pygame.transform.scale(self.image, size)
        elif image_name[0] == 'Animation':
            self.image = load_image(image_name[1])
        elif image_name[0] == 'Color':
            self.image = pygame.Surface(size)
            if form == 'circle':
                pygame.draw.circle(self.image, pygame.Color(image_name[1]),
                                   (size[0] // 2, size[1] // 2), size[0] // 2)
                self.image.set_colorkey(pygame.color.Color('black'))
            else:
                self.image.fill(pygame.color.Color(image_name[1]))
        self.rect = self.image.get_rect()
        if take_size:
            self.rect.w = size[0]
            self.rect.h = size[1]

    def update(self):
        pass

class Platform(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group[0])
        self.add(group[1])
        self.image = pygame.Surface([50, 10])
        pygame.draw.rect(self.image, pygame.Color("white"), (0, 0, 50, 10))
        self.rect = pygame.Rect(pos[0], pos[1], 50, 10)

class Box(Object):
    def __init__(self, group, pos):
        super().__init__(group[0], ('Image', 'box.png'))
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]

class Ground(Object):
    def __init__(self, group, pos=(-500, 0), size=(2000, 500)):
        super().__init__(group[0], ('Image', 'grassMid.png'), size, take_size=True)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]

class Wall(Object):
    def __init__(self, group, pos=(1500, -1000), size=(500, 1500)):
        super().__init__(group[0], ('Image', 'sandCenter.png'), size, take_size=True)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]

class Orb(Object):
    def __init__(self, group, pos, color):
        super().__init__(group[0], ('Color', color), (25, 25), take_size=True, form='circle', colorkey=-1)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]

class JumpOrb(Orb):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'red')

    def action(self, player):
        player.Vy = 7 * sign(player.G)

class GravityOrb(Orb):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'blue')

    def action(self, player):
        player.Vy = 2.5 * sign(player.G)
        player.G *= -1