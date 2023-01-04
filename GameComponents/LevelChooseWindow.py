import pygame
from .Window import Window, FPS, terminate, SIZE

class Level_Choise(Window):
    intro_text = ["Выберите уровень", ' ']
    text_coord_top = 50
    text_coord_left = 140
    font = pygame.font.Font(None, 30)

    def __init__(self, screen, file):
        super().__init__(screen, SIZE, ('Image', 'fon.jpg'))
        self.Lable = self.make_lines(self.intro_text)
        self.levels = self.get_level_list(file)
        self.buttons = self.make_buttons(self.levels.keys(), (self.text_coord_left,
                                                            self.text_coord_top + self.Lable.get_size()[1]))

    def show(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN:
                    pass
                for button in self.buttons:
                    last_pressed_button = button.update(event)
                    if last_pressed_button:
                        return last_pressed_button
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.Lable, (self.text_coord_left, self.text_coord_top))
            self.buttons.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()

    def get_level_list(self, filename):
        filename = "Data/" + filename
        levels = {}
        with open(filename, 'r') as levelsFile:
            for i in levelsFile.readlines():
                name, file = i.rstrip().split(':')
                levels[name] = file
        return levels