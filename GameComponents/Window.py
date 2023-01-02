import pygame
import sys
from .Imageloading import load_image

FPS = 50
SIZE = WIDTH, HEIGHT = 500, 500

def terminate():
    pygame.quit()
    sys.exit()

class Window:
    def __init__(self, screen, size=SIZE, background_fn=None):
        self.screen = screen
        if background_fn:
            self.background = pygame.transform.scale(load_image(background_fn), size)
        else:
            self.background = pygame.display.set_mode(size)
            self.background.fill(pygame.color.Color('cyan'))
        self.screen.blit(self.background, (0, 0))

    def show(self):
        clock = pygame.time.Clock()
        running = True
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