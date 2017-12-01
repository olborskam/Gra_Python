import time

import pygame


class GameScreen:
    def __init__(self, display, gameLogic):
        print("Painter init")
        self.display = display
        self.gameLogic = gameLogic
        background_img_name = self.gameLogic.background_img
        self.background = self.intialize_background(background_img_name)
        self.startGameTime = time.time()

    def intialize_background(self, background_img_name):
        background = pygame.image.load("resources/backgrounds/" + background_img_name).convert_alpha()
        screen = pygame.display.get_surface()
        screen.blit(background, (0, 0))
        pygame.display.flip()
        return background

    def draw(self):
        # Narysowanie tła na poprzednią klatke
        self.display.blit(self.background, (0, 0))

        # Narysowanie paletki
        self.display.blit(self.gameLogic.pad.draw(), self.gameLogic.pad.position)

        # Narysowanie klocków
        for brick in self.gameLogic.bricks:
            self.display.blit(brick.draw(), brick.position)

        # Narysowanie piłeczki
        ball = self.gameLogic.ball
        self.display.blit(ball.draw(), ball.position)

        # Narysowanie statystyk gry
        self.displayGameStats()

    def displayGameStats(self):
        font = pygame.font.SysFont("monospace", 12, True)
        points = font.render("Ilość żyć:" + str(self.gameLogic.lifes), True, (0, 0, 0), (255, 255, 255))
        gamepoints = font.render("Zdobyte punkty:" + str(self.gameLogic.gamepoints), True, (0, 0, 0), (255, 255, 255))
        gameTimeInSeconds = int(time.time() - self.startGameTime)
        gameTime = font.render("Czas gry:" + str(gameTimeInSeconds) + " sek", True, (0, 0, 0), (255, 255, 255))
        self.display.blit(points, (10, 10))
        self.display.blit(gamepoints, (10, 30))
        self.display.blit(gameTime, (10, 50))
