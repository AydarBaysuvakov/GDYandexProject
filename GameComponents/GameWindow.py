import pygame
from .Window import Window, FPS, terminate
from .Character import Character
from .Object import Stair, Box

class Game_Window(Window):
    def __init__(self, screen, level):
        self.level = level
        back = level['Background']
        super().__init__(screen, background_fn=back)

    def show(self):
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.stairs = pygame.sprite.Group()
        clock = pygame.time.Clock()
        self.player = None
        self.generate_level()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                if event.type == pygame.KEYDOWN:
                    if event.key == 1073741903:
                        self.player.walk(1)
                    if event.key == 1073741904:
                        self.player.walk(-1)
                    if event.key == 1073741906:
                        self.player.up(self, -1)
                    if event.key == 1073741905:
                        self.player.up(self, 1)
            self.screen.blit(self.background, (0, 0))
            self.player.update(self)
            self.all_sprites.draw(self.screen)
            clock.tick(FPS)
            pygame.display.flip()
        pygame.quit()

    def generate_level(self):
        self.size = self.level['Map_size']
        for item, value in self.level.items():
            if item == 'Player':
                self.player = Character(self.all_sprites, value[:2])
            if item == 'Box':
                for pos in value:
                    Box([self.all_sprites, self.platforms], pos[:2])
            if item == 'Stairs':
                for pos in value:
                    Stair([self.all_sprites, self.stairs], pos[:2])