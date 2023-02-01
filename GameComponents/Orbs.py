from .Object import Object

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


class Orb(Object):
    def __init__(self, group, pos, color):
        super().__init__(group[0], ('Color', color), (25, 25), take_size=True, form='circle', colorkey=-1)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        self.active = False


class JumpOrb(Orb):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'yellow')

    def action(self, player):
        if not self.active:
            player.Vy = 6 * sign(player.G)
        self.active = True


class GravityOrb(Orb):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'cyan')

    def action(self, player):
        if not self.active:
            player.Vy = 3 * sign(player.G)
            player.G *= -1
        self.active = True

class SmallJumpOrb(Orb):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'magenta')

    def action(self, player):
        if not self.active:
            player.Vy = 4 * sign(player.G)
        self.active = True


class BigJumpOrb(Orb):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'red')

    def action(self, player):
        if not self.active:
            player.Vy = 8 * sign(player.G)
        self.active = True


class ReverseOrb(Orb):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'green')

    def action(self, player):
        if not self.active:
            player.Vy = -6 * sign(player.G)
            player.G *= -1
        self.active = True


class PushOrb(Orb):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'white')

    def action(self, player):
        if not self.active:
            player.Vy = -10 * sign(player.G)
        self.active = True

class Jumppad(Object):
    def __init__(self, group, pos, color):
        super().__init__(group[0], ('Color', color), (40, 40), take_size=True, form='circle', colorkey=-1)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        self.active = False

class Jump(Jumppad):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'yellow')

    def action(self, player):
        if not self.active:
            player.Vy = 8 * sign(player.G)
        self.active = True

class SmallJump(Jumppad):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'magenta')

    def action(self, player):
        if not self.active:
            player.Vy = 6 * sign(player.G)
        self.active = True

class GravJump(Jumppad):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'cyan')

    def action(self, player):
        if not self.active:
            player.Vy = 3 * sign(player.G)
            player.G *= -1
        self.active = True

class BigJump(Jumppad):
    def __init__(self, group, pos):
        super().__init__(group, pos, 'red')

    def action(self, player):
        if not self.active:
            player.Vy = 10 * sign(player.G)
        self.active = True