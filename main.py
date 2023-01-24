import pygame
from GameComponents.Window import SIZE, TITLE, StartScreen, GameWindow, LevelChoise, Settings, Skins
from GameComponents.LoadComponents import load_level

if __name__ == '__main__':
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(TITLE)
    StartWindow = StartScreen(screen)
    Gamewindow = GameWindow(screen, load_level('test_level.txt'))
    setting = Settings(screen)
    skin = Skins(screen)
    Levels = LevelChoise(screen, 'Level_list.txt')
    running = True
    while running:
        last_pressed_button = StartWindow.show()
        if last_pressed_button == "Персонаж":
            skin.show()
        elif last_pressed_button == "Выбрать уровень":
            last_pressed_button = Levels.show()
            if last_pressed_button != 'back':
                Gamewindow = GameWindow(screen, load_level(Levels.levels[last_pressed_button]))
                last_pressed_button = Gamewindow.show()
        elif last_pressed_button == "Настройки":
            setting.show()
        while last_pressed_button == 'restart':
            Gamewindow.new_level()
            last_pressed_button = Gamewindow.show()