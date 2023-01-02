import pygame
from .Window import Window, FPS, SIZE, terminate
from .Character import Character

class Game_Window(Window):
    def __init__(self):
        super().__init__()

    def show(self):
        all_sprites = pygame.sprite.Group()
        platforms = pygame.sprite.Group()
        stairs = pygame.sprite.Group()
        clock = pygame.time.Clock()
        man = Character((-100, -100))
        ctrldown = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        all_sprites.remove(man)
                        man = Character(event.pos)
                    if event.button == 1 and ctrldown:
                        Stair(event.pos)
                    elif event.button == 1:
                        Platform(event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == 1073741903:
                        man.walk(1)
                    if event.key == 1073741904:
                        man.walk(-1)
                    if event.key == 1073741906:
                        man.up(-1)
                    if event.key == 1073741905:
                        man.up(1)
                    if event.key in (1073742048, 1073742052):
                        ctrldown = True
                if event.type == pygame.KEYUP:
                    if event.key in (1073742048, 1073742052):
                        ctrldown = False
            all_sprites.update()
            self.screen.fill(pygame.Color('black'))
            all_sprites.draw(self.screen)
            clock.tick(FPS)
            pygame.display.flip()
        pygame.quit()