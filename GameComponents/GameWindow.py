import pygame
from .Window import Window, terminate, FPS, Skins, Settings, StartScreen, LevelChoise, SIZE, TITLE
from .Button import RestartButton
from .Character import Cube, Ufo, Ball, Ship
from .Object import Box, Ground, Wall
from .Orbs import JumpOrb, GravityOrb, SmallJumpOrb, BigJumpOrb, ReverseOrb, PushOrb
from .Portals import GravityPortal, ShipPortal, UfoPortal, BallPortal, CubePortal
from .Portals import  SpeedPortal, Speed05xPortal, Speed15xPortal, UpPortal, DownPortal
from .Camera import Camera
from .LoadComponents import load_level

class GameWindow(Window):
    def __init__(self, screen, level):
        super().__init__(screen, background_fn=level['Background'])
        self.buttons = pygame.sprite.Group()
        self.backbtn = self.back_button(self.buttons)
        self.restart = RestartButton(self.buttons, (50, 8))
        self.level = level
        self.new_level()

    def new_level(self):
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.orbs = pygame.sprite.Group()
        self.portals = pygame.sprite.Group()
        self.camera = Camera()
        self.generate_level()

    def show(self):
        clock = pygame.time.Clock()
        running = True
        events = {}
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if self.backbtn.update(event):
                    return 'back'
                if self.restart.update(event):
                    return 'restart'
                if event.type == pygame.KEYDOWN:
                    events[event.key] = True
                    if event.key == pygame.K_ESCAPE:
                        return 'back'
                    if event.key == pygame.K_KP_0:
                        return 'restart'
                if event.type == pygame.KEYUP:
                    events[event.key] = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    events[event.button] = True
                if event.type == pygame.MOUSEBUTTONUP:
                    events[event.button] = False
            self.player.get_event(events)
            if self.player.event == 'restart':
                return 'restart'
            self.screen.blit(self.background, (0, 0))
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
        Ground([self.all_sprites, self.platforms], size=(self.size + 500, 500))
        Ground([self.all_sprites, self.platforms], size=(self.size + 500, 500), pos=(-500, -1000))
        Wall([self.all_sprites, self.platforms], (self.size, -1000))
        for item, value in self.level.items():
            if item == 'Player':
                if value[1] == 'Cube':
                    self.player = Cube(self.all_sprites, (value[0][0], -value[0][1]), self)
                if value[1] == 'Ball':
                    self.player = Ball(self.all_sprites, (value[0][0], -value[0][1]), self)
                if value[1] == 'Ship':
                    self.player = Ship(self.all_sprites, (value[0][0], -value[0][1]), self)
                if value[1] == 'Ufo':
                    self.player = Ufo(self.all_sprites, (value[0][0], -value[0][1]), self)
            if item == 'Box':
                for pos in value:
                    Box([self.all_sprites, self.platforms], (pos[0], -pos[1]))
            if item == 'Jump orb':
                for pos in value:
                    PushOrb([self.all_sprites, self.orbs], (pos[0], -pos[1]))
            if item == 'Gravity orb':
                for pos in value:
                    ReverseOrb([self.all_sprites, self.orbs], (pos[0], -pos[1]))
            if item == 'Gravity portal':
                for pos in value:
                    GravityPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
            if item == 'Ufo portal':
                for pos in value:
                    UfoPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
            if item == 'Speed1.5x':
                for pos in value:
                    Speed15xPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
            if item == 'Speed0.5x':
                for pos in value:
                    Speed05xPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)
        self.StartWindow = StartScreen(self.screen)
        self.setting = Settings(self.screen)
        self.skin = Skins(self.screen)
        self.Levels = LevelChoise(self.screen, 'Level_list.txt')

    def start(self):
        running = True
        while running:
            last_event = self.StartWindow.show()
            if last_event == "Выбрать уровень":
                last_event = self.Levels.show()
                if last_event != 'back':
                    self.Gamewindow = GameWindow(self.screen, load_level(self.Levels.levels[last_event]))
                    last_event = self.Gamewindow.show()
            elif last_event == "Персонаж":
                self.skin.show()
            elif last_event == "Настройки":
                self.setting.show()
            while last_event == 'restart':
                self.Gamewindow.new_level()
                last_event = self.Gamewindow.show()