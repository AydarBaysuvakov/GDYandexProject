from .Character import *

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

class Portal(Object):
    def __init__(self, group, pos, image_name, size=(40, 120)):
        super().__init__(group[0], ('Image', image_name), size=size, take_size=True)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        self.active = False

class ChangingCharacterPortal(Portal):
    def pick_sets(self, player):
        player.window.player.G = player.G
        player.window.player.Vx = player.Vx
        player.window.player.Vy = player.Vy
        player.window.player.coin = player.coin
        player.window.all_sprites.remove(player)

    def top(self, player):
        if player.window.top not in player.window.all_sprites:
            player.window.all_sprites.add(player.window.top)
            player.window.top.rect.x = player.window.ground.rect.x
            player.window.top.rect.y = player.window.ground.rect.y - 720

class GravityPortal(Portal):
    def __init__(self, group, pos, image_name='grav1.png'):
        super().__init__(group, pos, image_name)

    def action(self, player):
        if not self.active:
            player.Vy = sign(player.G)
            player.G *= -1
            player.reverse()
        self.active = True

class UpPortal(GravityPortal):
    def __init__(self, group, pos):
        super().__init__(group, pos)

    def action(self, player):
        if not self.active:
            player.Vy = sign(player.G)
            player.G = abs(player.G)
            player.reverse()
        self.active = True

class DownPortal(GravityPortal):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'grav2.png')

    def action(self, player):
        if not self.active:
            player.Vy = sign(player.G)
            player.G = -abs(player.G)
            player.reverse()
        self.active = True

class ShipPortal(ChangingCharacterPortal):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'shipportal.png')

    def action(self, player):
        if not self.active:
            player.window.player = Ship(player.window.all_sprites, (player.rect.x, player.rect.y), player.window)
            self.pick_sets(player)
            self.top(player)
        self.active = True

class CubePortal(ChangingCharacterPortal):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'cubeportal.png')

    def action(self, player):
        if not self.active:
            player.window.player = Cube(player.window.all_sprites, (player.rect.x, player.rect.y), player.window)
            self.pick_sets(player)
        self.active = True

class BallPortal(ChangingCharacterPortal):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'ballportal.png')

    def action(self, player):
        if not self.active:
            player.window.player = Ball(player.window.all_sprites, (player.rect.x, player.rect.y), player.window)
            self.pick_sets(player)
            self.top(player)
        self.active = True

class UfoPortal(ChangingCharacterPortal):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'ufoportal.png')

    def action(self, player):
        if not self.active:
            player.window.player = Ufo(player.window.all_sprites, (player.rect.x, player.rect.y), player.window)
            self.pick_sets(player)
            self.top(player)
        self.active = True

class SpeedPortal(Portal):
    SPEED = 4
    def __init__(self, group, pos, image_name='normal.png'):
        super().__init__(group, pos, image_name, size=(60, 120))

    def action(self, player):
        if not self.active:
            player.Vx = self.SPEED
        self.active = True

class FastSpeedPortal(SpeedPortal):
    SPEED = 8
    def __init__(self, group, pos):
        super().__init__(group, pos, 'fast.png')

class SlowSpeedPortal(SpeedPortal):
    SPEED = 2
    def __init__(self, group, pos):
        super().__init__(group, pos, 'slow.png')