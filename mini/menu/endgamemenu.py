import pygame
from pygame.constants import K_ESCAPE

# import mini.menu.mainmenu
# from mini import MENU_TICK_TIME
from mini.constants import SCREEN_NAME, SCREEN_SIZE, MENU_TICK_TIME
import mini.menu.mainmenu as mainmenu


class EndGameMenu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(SCREEN_NAME)
        self.fps = pygame.time.Clock()
        self.display = pygame.display.set_mode(SCREEN_SIZE)
        self.background = pygame.image.load("resources/backgrounds/back1.jpg").convert_alpha()
        self.font = pygame.font.Font('resources/fonts/Horrorshow.ttf', 30)
        self.font1 = pygame.font.Font('resources/fonts/Horrorshow.ttf', 50)

        text = self.font1.render("Game over", 1, (10, 10, 10))
        self.background.blit(text, (250, 100))

        text = self.font.render("Please push escape to return to main menu", 1, (10, 10, 10))
        self.background.blit(text, (30, 200))

        self.display.blit(self.background, (0, 0))
        pygame.display.flip()

        while True:
            self.fps.tick(MENU_TICK_TIME)
            for event in pygame.event.get():
                pressed = pygame.key.get_pressed()
                if pressed[K_ESCAPE]:
                    print("Return from")
                    menu = mainmenu.MainMenu()
                    menu.run()
                    # menu = mini.menu.mainmenu.MainMenu()
                    # menu.run()

            pygame.display.flip()
