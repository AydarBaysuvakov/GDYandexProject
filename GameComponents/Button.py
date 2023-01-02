import pygame
from .Imageloading import load_image

class Button(pygame.sprite.Sprite):
    btn_img = load_image("red_button_normal.png")
    btn_prsd_img = load_image("red_button_press.png")
    btn_hover_img = load_image("red_button_hover.png")
    font = pygame.font.Font(None, 30)

    def __init__(self, group, coords=(0, 0), text=''):
        super().__init__(group)
        self.image = self.btn_img.copy()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coords
        self.text = text
        self.text_write()

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos) or \
                args[-1][0] > 0 and self.rect.collidepoint(args[-1][1]):
            self.image = self.btn_prsd_img.copy()
            '''if args[-1][0] == 5:
                args[-1][2] = self.text'''
        elif args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.btn_hover_img.copy()
        else:
            self.image = self.btn_img.copy()
        self.text_write()

    def text_write(self):
        self.string_rendered = Button.font.render(self.text, 1, pygame.Color('white'))
        self.intro_rect = self.string_rendered.get_rect()
        self.intro_rect.top = 10
        self.intro_rect.x = 10
        self.image.blit(self.string_rendered, self.intro_rect)