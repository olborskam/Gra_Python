import pygame

from mini.constants import SCREEN_SIZE


class Pad(pygame.sprite.Sprite):
    def __init__(self):
        super(Pad, self).__init__()
        print("Pad init")
        self.width = 120
        self.height = 20
        self.position = [340, 580]
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.graphics = pygame.image.load("resources/pad/pad1a.png").convert_alpha()

    def draw(self):
        surface = pygame.Surface((self.width, self.height))
        surface.blit(self.graphics, (0, 0))
        return surface

    def move(self, delta):
        x = self.position[0]
        screen_width = SCREEN_SIZE[0]

        if 0 <= x + delta <= screen_width - self.width:
            self.position[0] += delta
            print("New position = " + str(self.position[0]))

    def x(self):
        return self.position[0]

    def y(self):
        return self.position[1]
