from .Object import Object

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


class Orb(Object):
    def __init__(self, group, pos, color):
        super().__init__(group[0], ('Color', color), (30, 30), take_size=True, form='circle', colorkey=-1)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]


class JumpOrb(Orb):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'yellow')

    def action(self, player):
        player.Vy = 7 * sign(player.G)


class GravityOrb(Orb):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'cyan')

    def action(self, player):
        player.Vy = 3 * sign(player.G)
        player.G *= -1


class SmallJumpOrb(Orb):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'magenta')

    def action(self, player):
        player.Vy = 6 * sign(player.G)


class BigJumpOrb(Orb):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'red')

    def action(self, player):
        player.Vy = 8 * sign(player.G)


class ReverseOrb(Orb):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'green')

    def action(self, player):
        player.Vy = -7 * sign(player.G)
        player.G *= -1


class PushOrb(Orb):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'white')

    def action(self, player):
        player.Vy = -10 * sign(player.G)