from .Object import Object
from .Character import Ship, Cube, Ball, Ufo

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

class Portal(Object):
    def __init__(self, group, pos, color):
        super().__init__(group[0], ('Color', color), (50, 150), take_size=True, colorkey=-1)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        self.active = False

class GravityPortal(Portal):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'cyan')

    def action(self, player):
        if not self.active:
            player.Vy = sign(player.G)
            player.G *= -1
        self.active = True

class ShipPortal(Portal):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'magenta')

    def action(self, player):
        if not self.active:
            player.window.player = Ship(player.window.all_sprites, (player.rect.x, player.rect.y), player.window)
            player.window.all_sprites.remove(player)
        self.active = True

class CubePortal(Portal):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'green')

    def action(self, player):
        if not self.active:
            player.window.player = Cube(player.window.all_sprites, (player.rect.x, player.rect.y), player.window)
            player.window.all_sprites.remove(player)
        self.active = True

class BallPortal(Portal):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'magenta')

    def action(self, player):
        if not self.active:
            player.window.player = Ball(player.window.all_sprites, (player.rect.x, player.rect.y), player.window)
            player.window.all_sprites.remove(player)
        self.active = True

class UfoPortal(Portal):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'magenta')

    def action(self, player):
        if not self.active:
            player.window.player = Ufo(player.window.all_sprites, (player.rect.x, player.rect.y), player.window)
            player.window.all_sprites.remove(player)
        self.active = True