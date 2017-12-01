import pygame
import sys
from pygame.constants import QUIT, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE

from mini.constants import BALL_VELOCITY, PAD_VELOCITY
import mini.menu.mainmenu

class KeyboardController(object):
    def __init__(self, gameLogic):
        self.gameLogic = gameLogic

    # Sterowanie gry - prawy, lewy, spacja
    def handle_game_events(self):
        pressed = pygame.key.get_pressed()

        # TODO: Uwzględnić stany gry
        if pressed[K_LEFT]:
            self.gameLogic.pad.move(-PAD_VELOCITY)
        if pressed[K_RIGHT]:
            self.gameLogic.pad.move(PAD_VELOCITY)
        if pressed[K_SPACE]:
            # Domyślnie piłeczka po wciśnięciu spacji leci w prawo
            self.gameLogic.ball.setVelocity([BALL_VELOCITY, -BALL_VELOCITY])

    # Sterowanie stanem gry:
    # Quit (krzyżyk) wyłącza gre,
    # Escape - pauza gry i ewentualnie menu w postaci przycisków:
    # 1. restart gry
    # 2. wróć do menu głównego (zakończ gre)
    # 3. wyłącz gre
    @staticmethod
    def handle_game_state_events(event):
        if event.type == QUIT:
            print("Quit game")
            sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[K_ESCAPE]:
            main_menu = mini.menu.mainmenu.MainMenu()
            main_menu.run()
