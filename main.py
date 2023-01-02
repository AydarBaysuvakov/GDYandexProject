import pygame
from GameComponents.Window import SIZE, TITLE
from GameComponents.StartScreen import Start_Screen
from GameComponents.GameWindow import Game_Window

if __name__ == '__main__':
    print('now_here')
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(TITLE)
    Start_Window = Start_Screen(screen)
    running = True
    while running:
        Start_Window.show()
        if Start_Window.params[2] == "Правила":
            pass
        elif Start_Window.params[2] == "Выбрать уровень":
            pass
        elif Start_Window.params[2] == "Начать игру":
            pass