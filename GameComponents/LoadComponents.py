import os
import sys
import pygame
import json

pygame.init()
screen = pygame.display.set_mode((800, 500))

def load_image(name, colorkey=None):
    fullname = os.path.join('Data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def load_level():
    with open('Data/levels.json') as level_file:
        return json.load(level_file)