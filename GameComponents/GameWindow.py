import pygame
from .Window import Window, terminate, FPS, Skins, Settings, StartScreen, LevelChoise, SIZE, TITLE
from .Button import RestartButton
from .Character import Cube, Ufo, Ball, Ship
from .Object import Box, Ground, WinZone
from .Orbs import JumpOrb, GravityOrb, SmallJumpOrb, BigJumpOrb, ReverseOrb, PushOrb, Jump, BigJump, GravJump, SmallJump
from .Portals import GravityPortal, ShipPortal, UfoPortal, BallPortal, CubePortal
from .Portals import  SpeedPortal, FastSpeedPortal, SlowSpeedPortal, UpPortal, DownPortal
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
        self.ground = Ground([self.all_sprites, self.platforms], size=(self.size + 500, 500))
        self.top = Ground([self.all_sprites, self.platforms], size=(self.size + 500, 400), pos=(self.ground.rect.x, self.ground.rect.y - 750))
        WinZone([self.all_sprites, self.platforms], (self.size, -1000))
        for item, value in self.level.items():
            if item == 'Player':
                if value[1] == 'Cube':
                    self.player = Cube(self.all_sprites, (value[0][0], -value[0][1]), self)
                    self.all_sprites.remove(self.top)
                if value[1] == 'Ball':
                    self.player = Ball(self.all_sprites, (value[0][0], -value[0][1]), self)
                if value[1] == 'Ship':
                    self.player = Ship(self.all_sprites, (value[0][0], -value[0][1]), self)
                if value[1] == 'Ufo':
                    self.player = Ufo(self.all_sprites, (value[0][0], -value[0][1]), self)
            # Коробка
            if item == 'Box':
                for pos in value:
                    Box([self.all_sprites, self.platforms], (pos[0], -pos[1]))
            # Орбы
            if item == 'Jump orb':
                for pos in value:
                    JumpOrb([self.all_sprites, self.orbs], (pos[0], -pos[1]))
            if item == 'Gravity orb':
                for pos in value:
                    GravityOrb([self.all_sprites, self.orbs], (pos[0], -pos[1]))
            if item == 'Small Jump orb':
                for pos in value:
                    SmallJumpOrb([self.all_sprites, self.orbs], (pos[0], -pos[1]))
            if item == 'Reverse orb':
                for pos in value:
                    ReverseOrb([self.all_sprites, self.orbs], (pos[0], -pos[1]))
            if item == 'Big Jump orb':
                for pos in value:
                    BigJumpOrb([self.all_sprites, self.orbs], (pos[0], -pos[1]))
            if item == 'Push orb':
                for pos in value:
                    PushOrb([self.all_sprites, self.orbs], (pos[0], -pos[1]))
            # Гравитационные порталы
            if item == 'Gravity portal':
                for pos in value:
                    GravityPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
            if item == 'Up portal':
                for pos in value:
                    UpPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
            if item == 'Down portal':
                for pos in value:
                    DownPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
            # Порталы смены персонажа
            if item == 'Ufo':
                for pos in value:
                    UfoPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
            if item == 'Cube':
                for pos in value:
                    CubePortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
            if item == 'Ship':
                for pos in value:
                    ShipPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
            if item == 'Ball':
                for pos in value:
                    BallPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
            # Порталы скорости
            if item == 'SpeedFast':
                for pos in value:
                    FastSpeedPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
            if item == 'SpeedSlow':
                for pos in value:
                    SlowSpeedPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
            if item == 'SpeedNormal':
                for pos in value:
                    SpeedPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
            # Jumppad
            if item == 'Jump':
                for pos in value:
                    Jump([self.all_sprites, self.portals], (pos[0], -pos[1]))
            if item == 'SmallJump':
                for pos in value:
                    SmallJump([self.all_sprites, self.portals], (pos[0], -pos[1]))
            if item == 'GravJump':
                for pos in value:
                    GravJump([self.all_sprites, self.portals], (pos[0], -pos[1]))
            if item == 'BigJump':
                for pos in value:
                    BigJump([self.all_sprites, self.portals], (pos[0], -pos[1]))

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