import pygame


class Brick(pygame.sprite.Sprite):
    NORMAL = 'NORMAL'
    SOLID = 'SOLID'
    WALL = 'WALL'

    def __init__(self, position, type):
        super(Brick, self).__init__()
        print("Brick init. state=" + type)
        self.position = position
        self.type = type

        self.image = pygame.image.load("resources/bricks/" + type + ".png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

    def draw(self):
        surface = pygame.Surface((self.width, self.height))
        surface.blit(self.image, (0, 0))
        return surface
