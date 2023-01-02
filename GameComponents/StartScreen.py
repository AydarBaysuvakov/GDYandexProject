import pygame
from .Window import Window, FPS, SIZE, terminate
from .Button import Button

class Start_Screen(Window):
    intro_text = ["SUPER MARIO BROS"]
    Button_text = ["Начать игру",
                   "Выбрать уровень",
                   "Правила"]
    text_coord_top = 50
    text_coord_left = 140
    font = pygame.font.Font(None, 30)

    def __init__(self, screen):
        super().__init__(screen, SIZE, 'fon.jpg')
        self.text_surface = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        top = self.text_coord_top + 60
        for line in self.Button_text:
            top += 10
            Button(self.buttons, (self.text_coord_left, top), line)
            top += 50

    def lines(self):
        top = self.text_coord_top
        for line in self.intro_text:
            string_rendered = self.font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            top += 10
            intro_rect.top = top
            intro_rect.x = self.text_coord_left
            top += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

    def show(self):
        clock = pygame.time.Clock()
        self.lines()
        # 0.prsd_anim_time, 1.last_pressed_pos, 2.prsd_btn(running)
        self.params = [0, (0, 0), False]
        while not self.params[2]:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:
                        print('enter')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.params = [10, event.pos] + [self.params[2]]
                self.buttons.update(event, self.params)
            self.params[0] = max(self.params[0] - 1, -1)
            self.lines()
            self.buttons.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()