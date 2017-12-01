import pygame

from mini.constants import *
from mini.gamelogic import GameLogic
from mini.gamescreen import GameScreen
from mini.keyboardcontroller import KeyboardController


#
# Klasa realizująca gre Arkanoid
#
class Game:
    def __init__(self, display=None, level=None):
        if display is None:
            self.display = self.pygame_init()
        else:
            self.display = display

        if level is None:
            self.level = "level.json"
        else:
            self.level = level

        self.fps = pygame.time.Clock()
        self.gameLogic = GameLogic(self.level)
        self.screen = GameScreen(self.display, self.gameLogic)
        self.keyboardController = KeyboardController(self.gameLogic)

    def pygame_init(self):
        pygame.init()
        pygame.mixer.init(11025)
        pygame.display.set_caption(SCREEN_NAME)
        display = pygame.display.set_mode(SCREEN_SIZE)
        return display

    def start(self):
        print("Game start")
        while True:
            self.loop()

    def loop(self):
        self.fps.tick(GAME_TICK_TIME)
        self.gameLogic.updateBallPosition()

        self.keyboardController.handle_game_events()
        for event in pygame.event.get():
            self.keyboardController.handle_game_state_events(event)

        # self.gameLogic.timer()
        self.screen.draw()
        pygame.display.update()
