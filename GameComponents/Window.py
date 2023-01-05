import pygame
import sys
from .LoadComponents import load_image
from .Button import RedButton, ReturnButton
from .Character import Player
from .Walls import Stair, Box
from .Camera import Camera
from .LineEdit import LineEdit

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

class StartScreen(Window):
    intro_text = ["SUPER MARIO BROS", ' ']
    Button_text = ["Начать игру",
                   "Выбрать уровень",
                   "Правила", 'For Rushan']
    text_coord_top = 50
    text_coord_left = 140
    font = pygame.font.Font(None, 30)

    def __init__(self, screen):
        super().__init__(screen, SIZE, ('Image', 'fon.jpg'))
        self.Lable = self.make_lines(self.intro_text)
        self.buttons = self.make_buttons(self.Button_text, (self.text_coord_left,
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

class LevelChoise(Window):
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
        self.backbtn = self.back_button(self.buttons)

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
                last_pressed_button = self.backbtn.update(event)
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

class Rules(Window):
    intro_text = ["Правила", ' ', 'Ходить: <- ->', 'Прыгать: ^', 'На лестницу можно залезть']
    text_coord_top = 50
    text_coord_left = 140
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN:
                    pass
                last_pressed_button = self.backbtn.update(event)
                if last_pressed_button:
                    return last_pressed_button
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.Lable, (self.text_coord_left, self.text_coord_top))
            self.buttons.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()

class GameWindow(Window):
    def __init__(self, screen, level):
        self.level = level
        back = level['Background']
        super().__init__(screen, background_fn=back)
        self.buttons = pygame.sprite.Group()
        self.backbtn = self.back_button(self.buttons)
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.stairs = pygame.sprite.Group()
        self.camera = Camera()
        self.generate_level()

    def show(self):
        clock = pygame.time.Clock()
        running = True
        pressed_buttons = []
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                last_pressed_button = self.backbtn.update(event)
                if last_pressed_button:
                    return last_pressed_button
                if event.type == pygame.KEYDOWN:
                    pressed_buttons.append(event.key)
                if event.type == pygame.KEYUP:
                    pressed_buttons.clear()
            for key in pressed_buttons:
                if key == pygame.K_RIGHT:
                    self.player.walk(1)
                if key == pygame.K_LEFT:
                    self.player.walk(-1)
                if key == pygame.K_UP:
                    if pygame.sprite.spritecollideany(self.player, self.stairs):
                        self.player.up(-1)
                    elif pygame.sprite.spritecollideany(self.player, self.platforms):
                        self.player.jump()
                if key == pygame.K_DOWN:
                    if pygame.sprite.spritecollideany(self.player, self.stairs):
                        self.player.up(1)
            self.screen.blit(self.background, (0, 0))
            self.player.update(self)
            self.all_sprites.draw(self.screen)
            self.camera.update(self.player)
            for sprite in self.all_sprites:
                self.camera.apply(sprite)
            self.buttons.draw(self.screen)
            clock.tick(FPS)
            pygame.display.flip()
        pygame.quit()

    def generate_level(self):
        self.size = self.level['Map_size']
        for item, value in self.level.items():
            if item == 'Player':
                self.player = Player(self.all_sprites, (value[0], -value[1]))
            if item == 'Box':
                for pos in value:
                    Box([self.all_sprites, self.platforms], (pos[0], -pos[1]))
            if item == 'Stairs':
                for pos in value:
                    Stair([self.all_sprites, self.stairs], (pos[0], -pos[1]))

class Settings(Window):
    def __init__(self, screen):
        super().__init__(screen, SIZE, ('Image', 'fon.jpg'))
        self.buttons = pygame.sprite.Group()
        self.lineedits = pygame.sprite.Group()
        for i in range(3):
            self.lineEdit = LineEdit(self.buttons, (100, 50 + 50 * i))
            self.lineEdit.add(self.lineedits)
        self.backbtn = self.back_button(self.buttons)

    def show(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                for button in self.buttons:
                    last_pressed_button = button.update(event, self)
                    if last_pressed_button:
                        return last_pressed_button
            self.screen.blit(self.background, (0, 0))
            self.buttons.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()