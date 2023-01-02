import pygame.display
from GameComponents.Window import SIZE
from GameComponents.StartScreen import Start_Screen

if __name__ == '__main__':
    screen = pygame.display.set_mode(SIZE)
    Start_Window = Start_Screen(screen)
    Start_Window.show()