from .Object import Object

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


class Orb(Object):
    JUMP_FORCE = None
    def __init__(self, group, pos, color):
        super().__init__(group[0], ('Color', color), (25, 25), take_size=True, form='circle', colorkey=-1)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        self.active = False

    def action(self, player):
        if not self.active:
            player.Vy = self.JUMP_FORCE * sign(player.G)
        self.active = True


class JumpOrb(Orb):
    JUMP_FORCE = 6
    def __init__(self, group, pos):
        super().__init__(group, pos, 'yellow')


class GravityOrb(Orb):
    JUMP_FORCE = 3
    def __init__(self, group, pos):
        super().__init__(group, pos, 'cyan')

    def action(self, player):
        if not self.active:
            player.Vy = self.JUMP_FORCE * sign(player.G)
            player.G *= -1
        self.active = True

class SmallJumpOrb(Orb):
    JUMP_FORCE = 4
    def __init__(self, group, pos):
        super().__init__(group, pos, 'magenta')


class BigJumpOrb(Orb):
    JUMP_FORCE = 8
    def __init__(self, group, pos):
        super().__init__(group, pos, 'red')


class ReverseOrb(Orb):
    JUMP_FORCE = -6
    def __init__(self, group, pos):
        super().__init__(group, pos, 'green')

    def action(self, player):
        if not self.active:
            player.Vy = self.JUMP_FORCE * sign(player.G)
            player.G *= -1
        self.active = True


class PushOrb(Orb):
    JUMP_FORCE = -10
    def __init__(self, group, pos):
        super().__init__(group, pos, 'white')

class Jumppad(Object):
    JUMP_FORCE = None
    def __init__(self, group, pos, color):
        super().__init__(group[0], ('Color', color), (40, 40), take_size=True, form='circle', colorkey=-1)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        self.active = False

class Jump(Jumppad):
    JUMP_FORCE = 8
    def __init__(self, group, pos):
        super().__init__(group, pos, 'yellow')

class SmallJump(Jumppad):
    JUMP_FORCE = 6
    def __init__(self, group, pos):
        super().__init__(group, pos, 'magenta')

class GravJump(Jumppad):
    JUMP_FORCE = 3
    def __init__(self, group, pos):
        super().__init__(group, pos, 'cyan')

    def action(self, player):
        if not self.active:
            player.Vy = self.JUMP_FORCE * sign(player.G)
            player.G *= -1
        self.active = True

class BigJump(Jumppad):
    JUMP_FORCE = 10
    def __init__(self, group, pos):
        super().__init__(group, pos, 'red')