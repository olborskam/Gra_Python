import sys

import pygame
from pygame.constants import K_UP, K_DOWN, K_RETURN

import mini
from mini.constants import MENU_TICK_TIME, SCREEN_NAME, X_BUTTON_OFFSET, Y_BUTTON_OFFSET, Y_BUTTONS_INTERVAL, SCREEN_SIZE
from mini.keyboardcontroller import KeyboardController
from mini.menu.aboutmenu import AboutMenu
from mini.menu.howtoplaymenu import HowToPlayMenu
from mini.menu.settingsmenu import SettingsMenu
from mini.menu.levelmenu import LevelMenu

class MainMenu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(SCREEN_NAME)
        self.fps = pygame.time.Clock()
        self.display = pygame.display.set_mode(SCREEN_SIZE)

        self.background = pygame.image.load("resources/backgrounds/mainMenu.png").convert_alpha()
        self.font = pygame.font.Font('resources/fonts/Horrorshow.ttf', 100)

        pygame.mixer.music.load('resources/backgrounds/music.wav')
        pygame.mixer.music.play(-1)
        self.active_button = 0
        self.captions = ["Play", "Settings", "How to play", "About", "Quit"]
        self.buttons = self.create_buttons(self.captions)

        self.display.blit(self.background, (0, 0))
        pygame.display.flip()

    def create_buttons(self, captions):
        buttons = []
        for i in range(len(captions)):
            button = self.font.render(captions[i], 1, (10, 10, 10))
            buttons.append(button)
            self.background.blit(button, calculate_button_position(i))
        return buttons

    def run(self):
        print("Menu run")
        while True:
            self.fps.tick(MENU_TICK_TIME)
            self.handle_menu_events()

            for event in pygame.event.get():
                KeyboardController.handle_game_state_events(event)

            self.display.blit(self.background, (0, 0))
            self.buttons[self.active_button] = self.font.render(self.captions[self.active_button], 1, (255, 10, 255))
            self.display.blit(self.buttons[self.active_button], calculate_button_position(self.active_button))
            pygame.display.update()

    def handle_menu_events(self):
        buttons_number = len(self.captions)
        pressed = pygame.key.get_pressed()

        if pressed[K_UP]:
            self.active_button = (self.active_button - 1) % buttons_number
            print('active_button=' + str(self.active_button))
        if pressed[K_DOWN]:
            self.active_button = (self.active_button + 1) % buttons_number
            print('active_button=' + str(self.active_button))
        if pressed[K_RETURN]:
            print("ENTER")
            self.change_screen(self.active_button)

    def change_screen(self, active_button):
        print(self.captions[active_button])

        if active_button == 0:
            levelMenu = LevelMenu(self.display)
            levelMenu.run()
        elif active_button == 1:
            print("MOCK settings")
            settingsMenu = SettingsMenu(self.display)
            settingsMenu.run()
        elif active_button == 2:
            print("MOCK how to play")
            howtoplayMenu = HowToPlayMenu(self.display)
        elif active_button == 3:
            print("MOCK about")
            aboutMenu = AboutMenu(self.display)
        elif active_button == 4:
            print("Quit game (Escape)")
            sys.exit()


def calculate_button_position(i):
    return X_BUTTON_OFFSET, Y_BUTTON_OFFSET + Y_BUTTONS_INTERVAL * i
