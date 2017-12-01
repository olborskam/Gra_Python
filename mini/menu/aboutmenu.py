import pygame
from pygame.constants import K_ESCAPE

import mini.menu.mainmenu
import mini


class AboutMenu:
    def __init__(self, display):
        self.display = display
        pygame.init()
        self.fps = pygame.time.Clock()
        self.background = pygame.image.load("resources/backgrounds/back1.jpg").convert_alpha()
        self.font = pygame.font.Font('resources/fonts/Horrorshow.ttf', 30)
        self.font1 = pygame.font.Font('resources/fonts/Horrorshow.ttf', 50)

        text = self.font1.render("About Game", 1, (10, 10, 10))
        self.background.blit(text, (250, 100))

        text = self.font.render("Gra zostala stworzona jako projekt zaliczeniowy ", 1, (10, 10, 10))
        self.background.blit(text, (30, 200))
        text = self.font.render("na przedmiot Przetwarzanie i Analiza Danych", 1, (10, 10, 10))
        self.background.blit(text, (30, 300))
        text = self.font.render("w Pythonie w roku akademickim 2017/2018", 1, (10, 10, 10))
        self.background.blit(text, (30, 400))

        self.display.blit(self.background, (0, 0))
        pygame.display.flip()

        while True:
            self.fps.tick(mini.MENU_TICK_TIME)
            for event in pygame.event.get():
                pressed = pygame.key.get_pressed()
                if pressed[K_ESCAPE]:
                    print("Return from")
                    menu = mini.menu.mainmenu.MainMenu()
                    menu.run()

            pygame.display.flip()
