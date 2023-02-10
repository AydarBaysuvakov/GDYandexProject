import pygame

WIDTH, HEIGHT = 800, 500
class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT * 3 // 4)

class Music:
    def __init__(self, file=None, start=0):
        pygame.mixer.music.set_volume(50)
        self.start = start
        self.file = 'Data/' + file
        pygame.mixer.music.load(self.file)

    def update(self, file=None, start=0):
        self.start = start
        self.file = 'Data/' + file
        pygame.mixer.music.load(self.file)

    def play(self):
        pygame.mixer.music.play(start=self.start)

    def restart(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.file)
        pygame.mixer.music.play(start=self.start)

    def stop(self):
        pygame.mixer.music.stop()

    def playing(self):
        return pygame.mixer.music.get_busy()

    def stoped_or_ended(self):
        return not pygame.mixer.music.get_busy()