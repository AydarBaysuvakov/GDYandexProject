import os
import sys
import pygame

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

def load_level(filename):
    filename = "Data/" + filename
    level = {}
    with open(filename, 'r') as mapFile:
        level['Background'] = mapFile.readline().rstrip().split(' / ')[1:]
        for line in mapFile.readlines():
            objects = line.rstrip().split(' / ')
            object_type, params = objects[0], objects[1:]
            if object_type == 'Map_size':
                level['Map_size'] = int(*params)
            elif object_type == 'Player':
                level['Player'] = list(map(int, params[0].split(', '))), params[1]
            else:
                level[object_type] = [[int(i) for i in p.split(', ')] for p in params]
    return level