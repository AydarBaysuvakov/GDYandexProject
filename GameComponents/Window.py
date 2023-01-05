import pygame
import sys
from .LoadComponents import load_image
from .Button import RedButton, ReturnButton

FPS = 50
TITLE = 'Mario Game'
SIZE = WIDTH, HEIGHT = 500, 500

def terminate():
    pygame.quit()
    sys.exit()

class Window:
    def __init__(self, screen, size=SIZE, background_fn=None):
        self.screen = screen
        if background_fn is None:
            self.background = pygame.Surface(self.screen.get_size())
            self.background.fill(pygame.color.Color('cyan'))
        elif background_fn[0] == 'Image':
            self.background = pygame.transform.scale(load_image(background_fn[1]), size)
        elif background_fn[0] == 'Animation':
            self.background = pygame.transform.scale(load_image(background_fn[1]), size)
        elif background_fn[0] == 'Color':
            self.background = pygame.Surface(self.screen.get_size())
            self.background.fill(pygame.color.Color(background_fn[1]))
        self.screen.blit(self.background, (0, 0))

    def make_lines(self, text):
        size = self.font.render(max(text, key=len), 1, pygame.Color('white')).get_rect()
        size.h *= len(text)
        text_surface = pygame.Surface((size.w, size.h)).convert()
        text_surface.fill('white')
        text_surface.set_colorkey(pygame.color.Color('white'))
        top, left = 0, 0
        for line in text:
            string_rendered = self.font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = top
            intro_rect.x = left
            top += intro_rect.height
            text_surface.blit(string_rendered, intro_rect)
        return text_surface

    def make_buttons(self, text, pos):
        buttons = pygame.sprite.Group()
        top = 0
        for line in text:
            top += 10
            RedButton(buttons, (pos[0], pos[1] + top), line)
            top += 50
        return buttons

    def back_button(self, group):
        return ReturnButton(group, (10, 10))

    def show(self):
        clock = pygame.time.Clock()
        running = True
        last_pressed_button = None
        while running:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN:
                    pass
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()