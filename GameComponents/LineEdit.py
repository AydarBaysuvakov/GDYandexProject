import pygame

class LineEdit(pygame.sprite.Sprite):
    def __init__(self, group, coords=(0, 0), text='', font=pygame.font.Font(None, 30)):
        super().__init__(group)
        self.image = pygame.Surface([250, 33])
        self.image.fill(pygame.color.Color('white'))
        self.rect = pygame.Rect(*coords, 250, 33)
        self.text, self.font = text, font
        self.choised = False

    def update(self, *args):
        if self.choised:
            if args and args[0].type == pygame.KEYDOWN:
                if args[0].key == pygame.K_BACKSPACE:
                    if self.text:
                        self.text = self.text[:-1]
                else:
                    self.text += args[0].unicode
            self.image.fill('yellow')
            self.text_write()
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            for i in args[1].lineedits:
                i.image.fill('white')
                i.text_write()
                i.choised = False
            self.choised = True

    def text_write(self):
        self.string_rendered = self.font.render(self.text, 1, pygame.Color('blue'))
        self.intro_rect = self.string_rendered.get_rect()
        self.intro_rect.top = 10
        self.intro_rect.x = 10
        self.image.blit(self.string_rendered, self.intro_rect)