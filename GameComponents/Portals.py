from .Character import *

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

class Portal(Object):
    def __init__(self, group, pos, color):
        super().__init__(group[0], ('Color', color), (30, 120), take_size=True, colorkey=-1)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        self.active = False

class ChangingCharacterPortal(Portal):
    def pick_sets(self, player):
        player.window.player.G = player.G
        player.window.player.Vx = player.Vx
        player.window.player.Vy = player.Vy
        player.window.all_sprites.remove(player)

    def top(self, player):
        if player.window.top not in player.window.all_sprites:
            player.window.all_sprites.add(player.window.top)
            player.window.top.rect.x = player.window.ground.rect.x
            player.window.top.rect.y = player.window.ground.rect.y - 700

class GravityPortal(Portal):
    def __init__(self, group, pos):
        super().__init__(group, pos, '#FFFFE0')

    def action(self, player):
        if not self.active:
            player.Vy = sign(player.G)
            player.G *= -1
        self.active = True

class UpPortal(GravityPortal):
    def action(self, player):
        if not self.active:
            player.Vy = sign(player.G)
            player.G = abs(player.G)
        self.active = True

class DownPortal(GravityPortal):
    def action(self, player):
        if not self.active:
            player.Vy = sign(player.G)
            player.G = -abs(player.G)
        self.active = True

class ShipPortal(ChangingCharacterPortal):
    def __init__(self, group, pos):
        super().__init__(group, pos, '#FF69B4')

    def action(self, player):
        if not self.active:
            player.window.player = Ship(player.window.all_sprites, (player.rect.x, player.rect.y), player.window)
            self.pick_sets(player)
            self.top(player)
        self.active = True

class CubePortal(ChangingCharacterPortal):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'yellow')

    def action(self, player):
        if not self.active:
            player.window.player = Cube(player.window.all_sprites, (player.rect.x, player.rect.y), player.window)
            self.pick_sets(player)
        self.active = True

class BallPortal(ChangingCharacterPortal):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'red')

    def action(self, player):
        if not self.active:
            player.window.player = Ball(player.window.all_sprites, (player.rect.x, player.rect.y), player.window)
            self.pick_sets(player)
            self.top(player)
        self.active = True

class UfoPortal(ChangingCharacterPortal):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'green')

    def action(self, player):
        if not self.active:
            player.window.player = Ufo(player.window.all_sprites, (player.rect.x, player.rect.y), player.window)
            self.pick_sets(player)
            self.top(player)
        self.active = True

class SpeedPortal(Portal):
    SPEED = 4
    def __init__(self, group, pos, color='#006400'):
        super().__init__(group, pos, color)

    def action(self, player):
        if not self.active:
            player.Vx = self.SPEED
        self.active = True

class FastSpeedPortal(SpeedPortal):
    SPEED = 8
    def __init__(self, group, pos):
        super().__init__(group, pos, '#FF4500')

class SlowSpeedPortal(SpeedPortal):
    SPEED = 2
    def __init__(self, group, pos):
        super().__init__(group, pos, '#20B2AA')