from .Window import Window, terminate, FPS, Skins, Settings, StartScreen, LevelChoise, SIZE, TITLE
from .Button import RestartButton
from .Object import *
from .Orbs import *
from .Portals import  *
from .Other import *
from .LoadComponents import load_level

class GameWindow(Window):
    def __init__(self, screen, level):
        super().__init__(screen, background_fn=level['Background'], music=level['Music'])
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
        self.spikes = pygame.sprite.Group()
        self.camera = Camera()
        self.generate_level()

    def show(self):
        clock = pygame.time.Clock()
        self.music.play()
        running = True
        events = {}
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if self.backbtn.update(event):
                    self.music.stop()
                    return 'back'
                if self.restart.update(event):
                    self.music.restart()
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
        # Размеры карты
        self.size = self.level['Map_size']
        # Пол, потолок и стена
        self.ground = Ground([self.all_sprites, self.platforms], size=(self.size + 500, 500))
        self.top = Ground([self.all_sprites, self.platforms], size=(self.size + 500, 400), pos=(self.ground.rect.x, self.ground.rect.y - 700))
        WinZone([self.all_sprites, self.platforms], (self.size, -1000))
        # Игрок
        self.Spawn_Player()
        # Объекты
        self.Spawn_Object()
        self.Spawn_Orbs()
        self.Spawn_Gravity_Portals()
        self.Spawn_Character_Change_Portals()
        self.Spawn_Speed_Portals()


    def Spawn_Player(self):
        if self.level['Player']['mode'] == 'Cube':
            self.player = Cube(self.all_sprites, (self.level['Player']['coords'][0], -self.level['Player']['coords'][1]), self)
            self.all_sprites.remove(self.top)
        if self.level['Player']['mode'] == 'Ball':
            self.player = Ball(self.all_sprites, (self.level['Player']['coords'][0], -self.level['Player']['coords'][1]), self)
        if self.level['Player']['mode'] == 'Ship':
            self.player = Ship(self.all_sprites, (self.level['Player']['coords'][0], -self.level['Player']['coords'][1]), self)
        if self.level['Player']['mode'] == 'Ufo':
            self.player = Ufo(self.all_sprites, (self.level['Player']['coords'][0], -self.level['Player']['coords'][1]), self)

    def Spawn_Object(self):
        if 'Box' in self.level:
            for pos in self.level['Box']:
                Box([self.all_sprites, self.platforms], (pos[0], -pos[1]))
        if 'Spike' in self.level:
            for pos in self.level['Spike']:
                Spike([self.all_sprites, self.spikes], (pos[0], -pos[1]))
        if 'Coin' in self.level:
            for pos in self.level['Coin']:
                Coin([self.all_sprites, self.portals], (pos[0], -pos[1]))

    def Spawn_Orbs(self):
        if 'Jump Orb' in self.level:
            for pos in self.level['Jump Orb']:
                JumpOrb([self.all_sprites, self.orbs], (pos[0], -pos[1]))
        if 'Gravity Orb' in self.level:
            for pos in self.level['Gravity Orb']:
                GravityOrb([self.all_sprites, self.orbs], (pos[0], -pos[1]))
        if 'Small Jump Orb' in self.level:
            for pos in self.level['Small Jump Orb']:
                SmallJumpOrb([self.all_sprites, self.orbs], (pos[0], -pos[1]))
        if 'Reverse Orb' in self.level:
            for pos in self.level['Reverse Orb']:
                ReverseOrb([self.all_sprites, self.orbs], (pos[0], -pos[1]))
        if 'Big Jump Orb' in self.level:
            for pos in self.level['Big Jump Orb']:
                BigJumpOrb([self.all_sprites, self.orbs], (pos[0], -pos[1]))
        if 'Push Orb' in self.level:
            for pos in self.level['Push Orb']:
                PushOrb([self.all_sprites, self.orbs], (pos[0], -pos[1]))

    def Spawn_Gravity_Portals(self):
        if 'Gravity portal' in self.level:
            for pos in self.level['Gravity Portal']:
                GravityPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
        if 'Up portal' in self.level:
            for pos in self.level['Up Portal']:
                UpPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
        if 'Down portal' in self.level:
            for pos in self.level['Down Portal']:
                DownPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))

    def Spawn_Character_Change_Portals(self):
        if 'Ufo' in self.level:
            for pos in self.level['Ufo']:
                UfoPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
        if 'Cube' in self.level:
            for pos in self.level['Cube']:
                CubePortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
        if 'Ship' in self.level:
            for pos in self.level['Ship']:
                ShipPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
        if 'Ball' in self.level:
            for pos in self.level['Ball']:
                BallPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))

    def Spawn_Speed_Portals(self):
        if 'SpeedFast' in self.level:
            for pos in self.level['SpeedFast']:
                FastSpeedPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
        if 'SpeedSlow' in self.level:
            for pos in self.level['SpeedSlow']:
                SlowSpeedPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))
        if 'SpeedNormal' in self.level:
            for pos in self.level['SpeedNormal']:
                SpeedPortal([self.all_sprites, self.portals], (pos[0], -pos[1]))

    def Spawn_Jumppads(self):
        if 'Jump' in self.level:
            for pos in self.level['Jump']:
                Jump([self.all_sprites, self.portals], (pos[0], -pos[1]))
        if 'SmallJump' in self.level:
            for pos in self.level['SmallJump']:
                SmallJump([self.all_sprites, self.portals], (pos[0], -pos[1]))
        if 'GravJump' in self.level:
            for pos in self.level['GravJump']:
                GravJump([self.all_sprites, self.portals], (pos[0], -pos[1]))
        if 'BigJump' in self.level:
            for pos in self.level['BigJump']:
                BigJump([self.all_sprites, self.portals], (pos[0], -pos[1]))


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)
        self.StartWindow = StartScreen(self.screen)
        self.setting = Settings(self.screen)
        self.skin = Skins(self.screen)
        self.Levels = LevelChoise(self.screen)

    def start(self):
        running = True
        while running:
            last_event = self.StartWindow.show()
            if last_event == "Выбрать уровень":
                last_event = self.Levels.show()
                if last_event != 'back':
                    self.Gamewindow = GameWindow(self.screen, load_level()[last_event])
                    last_event = self.Gamewindow.show()
            elif last_event == "Персонаж":
                self.skin.show()
            elif last_event == "Редактор":
                self.setting.show()
            while last_event == 'restart':
                self.Gamewindow.new_level()
                last_event = self.Gamewindow.show()