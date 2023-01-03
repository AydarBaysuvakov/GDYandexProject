import pygame
from .Window import Window, FPS, SIZE, terminate

class Start_Screen(Window):
    intro_text = ["SUPER MARIO BROS", ' ']
    Button_text = ["Начать игру",
                   "Выбрать уровень",
                   "Правила"]
    text_coord_top = 50
    text_coord_left = 140
    font = pygame.font.Font(None, 30)

    def __init__(self, screen):
        super().__init__(screen, SIZE, 'fon.jpg')
        self.Lable = self.make_lines(self.intro_text)
        self.buttons = self.make_buttons(self.Button_text, (self.text_coord_left,
                                                            self.text_coord_top + self.Lable.get_size()[1]))

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
                for button in self.buttons:
                    last_pressed_button = button.update(event)
                    if last_pressed_button:
                        return last_pressed_button
            self.screen.blit(self.Lable, (self.text_coord_left, self.text_coord_top))
            self.buttons.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()