import json

import pygame
from pygame.constants import K_UP, K_DOWN, K_RETURN

import mini
from mini.constants import MENU_TICK_TIME, SCREEN_NAME, X_BUTTON_OFFSET, Y_BUTTON_OFFSET, Y_BUTTONS_INTERVAL, SCREEN_SIZE
from mini.keyboardcontroller import KeyboardController


class SettingsMenu:
    def __init__(self, display):
        pygame.init()
        pygame.display.set_caption(SCREEN_NAME)
        self.fps = pygame.time.Clock()
        self.display = pygame.display.set_mode(SCREEN_SIZE)

        self.background = pygame.image.load("resources/backgrounds/back1.jpg").convert_alpha()
        self.font = pygame.font.Font('resources/fonts/Horrorshow.ttf', 30)

        file = json.load(open("resources/settings.json"))
        self.lifes = file["lifes"]
        self.padVelocity = file["padVelocity"]
        self.ballVelocity = file["ballVelocity"]

        self.font = pygame.font.Font('resources/fonts/Horrorshow.ttf', 30)
        self.font1 = pygame.font.Font('resources/fonts/Horrorshow.ttf', 50)
        text = self.font1.render("Settings", 1, (10, 10, 10))
        self.background.blit(text, (300, 100))

        text = self.font.render("Wybierz liczbe zyc:", 1, (10, 10, 10))
        self.background.blit(text, (30, 200))

        self.active_button = int(self.lifes / 2)
        self.captions = ["1", "3", "5"]
        self.buttons = self.create_buttons(self.captions)

        self.display.blit(self.background, (0, 0))
        pygame.display.flip()

    def change_lifes(self, active_button):
        print(self.captions[active_button])
        if active_button == 0:
            self.lifes = 1
        elif active_button == 1:
            self.lifes = 3
        elif active_button == 2:
            self.lifes = 5

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
            self.lifes = 2 * self.active_button + 1
            self.save_settings_to_json()
            menu = mini.menu.mainmenu.MainMenu()
            menu.run()

    def save_settings_to_json(self):
        with open('resources/settings.json', 'w') as outfile:
            data = {}
            data['lifes'] = self.lifes
            data['padVelocity'] = self.padVelocity
            data['ballVelocity'] = self.ballVelocity
            json.dump(data, outfile)


def calculate_button_position(i):
    return X_BUTTON_OFFSET, Y_BUTTON_OFFSET + Y_BUTTONS_INTERVAL * i + 220
