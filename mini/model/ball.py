import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        print("Ball init")
        self.position = [0, 0]
        self.velocity = [0, 0]
        self.width = 40
        self.height = 40

        self.image = pygame.image.load("resources/ball/ball-40px.png").convert_alpha()
        self.rect = self.image.get_rect()

    def draw(self):
        surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        surface.blit(self.image, (0, 0))
        return surface

    def setPos(self, x, y):
        self.position[0] = x
        self.position[1] = y

    def setVelocity(self, velocity):
        self.velocity = velocity

    def move(self):
        x = self.position[0]
        y = self.position[1]
        self.position[0] = x + self.velocity[0]
        self.position[1] = y + self.velocity[1]

    def x(self):
        return self.position[0]

    def y(self):
        return self.position[1]

    def inverse_velocity_x(self):
        self.velocity[0] = -self.velocity[0]

    def inverse_velocity_y(self):
        self.velocity[1] = -self.velocity[1]

    def collision(self, obj):
        x1 = self.position[0]
        x2 = self.position[0] + self.width
        y1 = self.position[1]
        y2 = self.position[1] + self.height

        a1 = obj.position[0]
        a2 = obj.position[0] + obj.width
        b1 = obj.position[1]
        b2 = obj.position[1] + obj.height
        return x1 <= a2 and x2 >= a1 and y1 < b2 and y2 > b1


    def printBallPosition(self):
        print("ball (x,y)=(" + str(self.x()) + "," + str(self.y()) + ")")

