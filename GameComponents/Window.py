import pygame
import sys
import json
from .LoadComponents import load_image, load_level
from .Button import RedButton, ReturnButton, ChrButton
from .Other import Music

FPS = 60
TITLE = 'Geometry dash'
SIZE = WIDTH, HEIGHT = 800, 500

def terminate():
    pygame.quit()
    sys.exit()

class Window:
    def __init__(self, screen, size=SIZE, background_fn=None, coords=(0, 0), music=('Theme.mp3', 0)):
        self.set_screen(screen, size, background_fn, coords)
        self.set_music(*music)

    def set_screen(self, screen, size=SIZE, background_fn=None, coords=(0, 0)):
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
        self.screen.blit(self.background, coords)

    def set_music(self, file, start=0):
        self.music = Music(file, start)

    def make_lines(self, text):
        size = self.font.render(max(text, key=len), 1, pygame.Color('white')).get_rect()
        size.h *= len(text)
        text_surface = pygame.Surface((size.w, size.h)).convert()
        text_surface.fill('white')
        text_surface.set_colorkey(pygame.color.Color('white'))
        top, left = 0, 0
        for line in text:
            string_rendered = self.font.render(line, 1, pygame.Color('yellow'))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = top
            intro_rect.x = left
            top += intro_rect.height
            text_surface.blit(string_rendered, intro_rect)
        return text_surface

    def make_buttons(self, group, text, pos):
        top = 0
        for line in text:
            RedButton(group, (pos[0], pos[1] + top), line)
            top += 60

    def back_button(self, group):
        return ReturnButton(group, (8, 8))

    def show(self):
        clock = pygame.time.Clock()
        running = True
        last_event = None
        while running:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()

class StartScreen(Window):
    intro_text = ["Geometry dash", ' ']
    Button_text = ["Выбрать уровень",
                   "Персонаж",
                   "Редактор"]
    text_coord_top = 50
    text_coord_left = 300
    font = pygame.font.Font(None, 30)

    def __init__(self, screen):
        super().__init__(screen, background_fn=('Image', 'fon.jpg'))
        self.Lable = self.make_lines(self.intro_text)
        self.buttons = pygame.sprite.Group()
        self.make_buttons(self.buttons, self.Button_text,
                          (self.text_coord_left, self.text_coord_top + self.Lable.get_size()[1]))

    def show(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            if self.music.stoped_or_ended():
                self.music.restart()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                for button in self.buttons:
                    last_event = button.update(event)
                    if last_event:
                        return last_event
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.Lable, (self.text_coord_left, self.text_coord_top))
            self.buttons.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()

class LevelChoise(Window):
    StartSound = pygame.mixer.Sound('Data/Click.mp3')
    StartSound.set_volume(100)
    intro_text = ["Выберите уровень", ' ']
    text_coord_top = 50
    text_coord_left = 300
    font = pygame.font.Font(None, 30)

    def __init__(self, screen):
        super().__init__(screen, background_fn=('Image', 'fon.jpg'))
        self.Lable = self.make_lines(self.intro_text)
        self.levels = self.get_level_list()
        self.buttons = pygame.sprite.Group()
        self.make_buttons(self.buttons, self.levels,
                          (self.text_coord_left, self.text_coord_top + self.Lable.get_size()[1]))
        self.backbtn = self.back_button(self.buttons)

    def show(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            if self.music.stoped_or_ended():
                self.music.restart()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                for button in self.buttons:
                    last_event = button.update(event)
                    if last_event:
                        self.StartSound.play()
                        return last_event
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.Lable, (self.text_coord_left, self.text_coord_top))
            self.buttons.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()

    def get_level_list(self):
        levels = load_level().keys()
        return levels

class Settings(Window):
    intro_text = ["Soon"]
    text_coord_top = 50
    text_coord_left = 380
    font = pygame.font.Font(None, 30)

    def __init__(self, screen):
        super().__init__(screen, SIZE, ('Image', 'fon.jpg'))
        self.Lable = self.make_lines(self.intro_text)
        self.buttons = pygame.sprite.Group()
        self.backbtn = self.back_button(self.buttons)

    def show(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            if self.music.stoped_or_ended():
                self.music.restart()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                last_event = self.backbtn.update(event)
                if last_event:
                    return last_event
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.Lable, (self.text_coord_left, self.text_coord_top))
            self.buttons.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()

class Skins(Window):
    intro_text = ["Выберите персонажа"]
    text_coord_top = 50
    text_coord_left = 340
    btn_top = 250
    btn_left = 100
    font = pygame.font.Font(None, 30)

    def __init__(self, screen):
        super().__init__(screen, SIZE, ('Image', 'fon.jpg'))
        self.Lable = self.make_lines(self.intro_text)
        self.buttons = pygame.sprite.Group()
        self.backbtn = self.back_button(self.buttons)
        self.get_skins()
        self.mode = 'cube'
        self.make_buttons(self.buttons, 'cubes', (self.btn_left, self.btn_top))


    def show(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            if self.music.stoped_or_ended():
                self.music.restart()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                for button in self.buttons:
                    last_event = button.update(event)
                    if last_event == 'back':
                        return last_event
                    if last_event:
                        if last_event.startswith('-'):
                            self.change_mode(last_event[1:].split('.')[0])
                        else:
                            self.change_skin(last_event)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.Lable, (self.text_coord_left, self.text_coord_top))
            self.buttons.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()

    def make_buttons(self, group, text, pos):
        right = 0
        for key, value in self.skins.items():
            ChrButton(group, value['curent'], (pos[0] + right + 50, pos[1] - 70), '-' + value['curent'])
            right += 60
        right = 0
        other = self.skins[text]['others']
        for line in other:
            ChrButton(group, line, (pos[0] + right, pos[1]), line)
            right += 60

    def get_skins(self):
        with open('Data/skins.json') as skin_file:
            self.skins = json.load(skin_file)

    def change_skin(self, skin):
        self.skins[self.mode + 's']['curent'] = skin
        with open('Data/skins.json', 'w') as skin_file:
            json.dump(self.skins, skin_file)
            skin_file.close()
        self.buttons.empty()
        self.backbtn = self.back_button(self.buttons)
        self.get_skins()
        self.make_buttons(self.buttons, self.mode + 's', (self.btn_left, self.btn_top))

    def change_mode(self, mode):
        self.mode = mode[:-1]
        self.buttons.empty()
        self.backbtn = self.back_button(self.buttons)
        self.get_skins()
        self.make_buttons(self.buttons, self.mode + 's', (self.btn_left, self.btn_top))