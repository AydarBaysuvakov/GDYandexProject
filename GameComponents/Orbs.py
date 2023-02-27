from .Object import Object

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


class Orb(Object):
    JUMP_FORCE = None
    def __init__(self, group, pos, image_name):
        super().__init__(group[0], ('Image', image_name), (25, 25), take_size=True, form='circle', colorkey=-1)
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
        super().__init__(group, pos, 'orb1.png')


class GravityOrb(Orb):
    JUMP_FORCE = 3
    def __init__(self, group, pos):
        super().__init__(group, pos, 'orb4.png')

    def action(self, player):
        if not self.active:
            player.Vy = self.JUMP_FORCE * sign(player.G)
            player.G *= -1
            player.reverse()
        self.active = True

class SmallJumpOrb(Orb):
    JUMP_FORCE = 4
    def __init__(self, group, pos):
        super().__init__(group, pos, 'orb2.png')


class BigJumpOrb(Orb):
    JUMP_FORCE = 9
    def __init__(self, group, pos):
        super().__init__(group, pos, 'orb3.png')


class ReverseOrb(Orb):
    JUMP_FORCE = -6
    def __init__(self, group, pos):
        super().__init__(group, pos, 'orb5.png')

    def action(self, player):
        if not self.active:
            player.Vy = self.JUMP_FORCE * sign(player.G)
            player.G *= -1
            player.reverse()
        self.active = True


class PushOrb(Orb):
    JUMP_FORCE = -10
    def __init__(self, group, pos):
        super().__init__(group, pos, 'orb6.png')

class Jumppad(Object):
    JUMP_FORCE = None
    def __init__(self, group, pos, image_name):
        super().__init__(group[0], ('Image', image_name), (40, 20), take_size=True)
        self.add(group[1])
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        self.active = False

    def action(self, player):
        if not self.active:
            player.Vy = self.JUMP_FORCE * sign(player.G)
        self.active = True

class Jump(Jumppad):
    JUMP_FORCE = 8
    def __init__(self, group, pos):
        super().__init__(group, pos, 'jumppad1.png')

class SmallJump(Jumppad):
    JUMP_FORCE = 6
    def __init__(self, group, pos):
        super().__init__(group, pos, 'jumppad2.png')

class GravJump(Jumppad):
    JUMP_FORCE = 3
    def __init__(self, group, pos):
        super().__init__(group, pos, 'jumppad3.png')

    def action(self, player):
        if not self.active:
            player.Vy = self.JUMP_FORCE * sign(player.G)
            player.G *= -1
            player.reverse()
        self.active = True

class BigJump(Jumppad):
    JUMP_FORCE = 10
    def __init__(self, group, pos):
        super().__init__(group, pos, 'jumppad4.png')