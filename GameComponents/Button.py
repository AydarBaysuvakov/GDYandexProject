import pygame
from .LoadComponents import load_image

class Button(pygame.sprite.Sprite):
    def __init__(self, group, image, coords=(0, 0), text='', font=pygame.font.Font(None, 30), size=None):
        super().__init__(group)
        self.image = image.copy()
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coords
        self.text, self.font = text, font
        self.pressed = 0

    def update(self, *args):
        if self.pressed >= 2:
            self.pressed = 0
            return self.text
        elif 0 < self.pressed:
            self.pressed += 1
        elif args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.pressed += 1

    def text_write(self):
        self.string_rendered = self.font.render(self.text, 1, pygame.Color('blue'))
        self.intro_rect = self.string_rendered.get_rect()
        self.intro_rect.top = 10
        self.intro_rect.x = 10
        self.image.blit(self.string_rendered, self.intro_rect)

class RedButton(Button):
    btn_img = load_image("red_button_normal.png")
    btn_prsd_img = load_image("red_button_press.png")
    btn_hover_img = load_image("red_button_hover.png")

    def __init__(self, group, coords=(0, 0), text='', size=None):
        super().__init__(group, self.btn_img, coords, text, size=size)
        self.size = size
        self.text_write()

    def update(self, *args):
        if self.pressed >= 2:
            self.pressed = 0
            return self.text
        elif 0 < self.pressed:
            self.pressed += 1
        elif args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.pressed += 1
            self.image = self.btn_prsd_img.copy()
        elif args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.btn_hover_img.copy()
        else:
            self.image = self.btn_img.copy()
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)
        self.text_write()

class ReturnButton(Button):
    image = pygame.transform.scale(load_image('back.png'), (35, 35))
    def __init__(self, group, coords=(0, 0)):
        super().__init__(group, self.image, coords, text='back')

class RestartButton(Button):
    image = pygame.transform.scale(load_image('star1.png'), (35, 35))
    def __init__(self, group, coords=(0, 0)):
        super().__init__(group, self.image, coords, text='restart')

class ChrButton(Button):
    def __init__(self, group, image, coords=(0, 0), text='', size=[50, 50], back_color='cyan'):
        self.image = pygame.Surface(size)
        self.image.fill(pygame.color.Color(back_color))
        super().__init__(group, self.image, size=(50, 50), text=text, coords=coords)
        self.skin = pygame.transform.scale(load_image(image, colorkey=None), (40, 40))
        self.image.blit(self.skin, (5, 5))