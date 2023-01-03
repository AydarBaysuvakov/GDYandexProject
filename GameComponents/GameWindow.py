import pygame
from .Window import Window, FPS, terminate
from .Character import Character
from .Object import Stair, Box
from .Levelloading import load_level

class Game_Window(Window):
    def __init__(self, screen):
        super().__init__(screen)

    def show(self):
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.stairs = pygame.sprite.Group()
        clock = pygame.time.Clock()
        player = None
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        self.all_sprites.remove(man)
                        man = Character(self.all_sprites, event.pos)
                    if event.button == 1 and ctrldown:
                        Stair((self.all_sprites, self.stairs), event.pos)
                    elif event.button == 1:
                        Box((self.all_sprites, self.platforms), event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == 1073741903:
                        man.walk(1)
                    if event.key == 1073741904:
                        man.walk(-1)
                    if event.key == 1073741906:
                        man.up(self, -1)
                    if event.key == 1073741905:
                        man.up(self, 1)
                    if event.key in (1073742048, 1073742052):
                        ctrldown = True
                if event.type == pygame.KEYUP:
                    if event.key in (1073742048, 1073742052):
                        ctrldown = False
            self.screen.blit(self.background, (0, 0))
            man.update(self)
            self.all_sprites.draw(self.screen)
            clock.tick(FPS)
            pygame.display.flip()
        pygame.quit()

    def generate_level(self, level):
        size = right, top, left = level['Map_size']
        for item, value in level.items():
            if item == 'Player':
                player = ''
        return player, size