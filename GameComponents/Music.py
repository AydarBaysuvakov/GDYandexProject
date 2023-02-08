import pygame

class Music:
    def __init__(self, file):
        pygame.mixer.music.load(file)

    def play(self):
        pygame.mixer.music.play(start=20)

    def restart(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.play(start=20)

    def stop(self):
        pygame.mixer.music.stop()