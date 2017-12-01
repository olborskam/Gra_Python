import json

import mini
import mini.menu.endgamemenu
from mini.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from mini.model.ball import Ball
from mini.model.brick import Brick
from mini.model.pad import Pad


class GameLogic():
    def __init__(self, level):
        print("GameLogic init")
        self.pad = Pad()
        self.ball = Ball()

        file = json.load(open("resources/levels/" + level))
        self.bricks = self.load_bricks_from_json(file)
        self.level_name = file["level_name"]
        self.background_img = file["background_img"]
        self.lifes = mini.constants.load_lifes_from_json()
        self.bricklifes = 2
        self.gamepoints = 0
        self.n = 30

    def load_bricks_from_json(self, file):
        bricks_from_json = file["bricks"]
        bricks = []
        for brick in bricks_from_json:
            x = brick["position"]["x"]
            y = brick["position"]["y"]
            bricks.append(Brick([x, y], brick["type"]))
        return bricks

    def updateBallPosition(self):
        if self.ball.velocity == [0, 0]:
            x = self.pad.x() + 0.5 * self.pad.width - 0.5 * self.ball.width
            y = self.pad.y() - self.ball.height
            # self.ball.setPos(x, y)
            self.ball.setPos(self.pad.x(), self.pad.y() - self.ball.height)
        else:
            self.handleCollision()
            self.ball.move()

    def handleCollision(self):
        self.ball.printBallPosition()
        self.handle_collision_with_screen_bound(self.ball)
        self.handle_collision_with_brick(self.ball)
        self.handle_collision_with_pad(self.ball)

    def handle_collision_with_screen_bound(self, ball):
        x = ball.x()
        y = ball.y()

        # Kolizja z prawą ścianą
        if (SCREEN_WIDTH - 0.5 * self.ball.width <= x <= SCREEN_WIDTH) and self.ball.velocity[0] > 0:
            self.ball.velocity[0] = -self.ball.velocity[0]

        # Kolizja z lewą ścianą
        if (0 <= x <= 0 + 0.5 * self.ball.width) and self.ball.velocity[0] < 0:
            self.ball.velocity[0] = -self.ball.velocity[0]

        # Kolizja z górną ścianą
        if (0 <= y <= 0 + 0.5 * self.ball.height) and self.ball.velocity[1] < 0:
            self.ball.velocity[1] = -self.ball.velocity[1]

        # Kolizja z dolną ścianą
        if (SCREEN_HEIGHT - 0.5 * self.ball.height <= y <= SCREEN_HEIGHT) and self.ball.velocity[1] > 0:
            print("TRACISZ ŻYCIE")
            # Zliczanie ilosci zyc do konca gry
            self.ball.setVelocity([0, 0])
            self.lifes = self.lifes - 1
            if self.lifes == 0:
                print("GAME OVER")
                endGameMenu = mini.menu.endgamemenu.EndGameMenu()

    def handle_collision_with_brick(self, ball):
        for brick in self.bricks:
            if ball.collision(brick):
                # sprawdzenie jaki to rodzaj klocka: normal, wall czy solid
                if brick.type == "NORMAL":
                    print("collision ball with normal brick")
                    self.bricks.remove(brick)
                    self.ball.inverse_velocity_y()
                    self.gamepoints = self.gamepoints + 1
                elif brick.type == "WALL":
                    print("collision ball with  wall brick")
                    self.ball.inverse_velocity_y()
                else:
                    print("collision ball with solid brick")
                    self.bricklifes = self.bricklifes - 1
                    self.ball.inverse_velocity_y()
                    self.gamepoints = self.gamepoints + 1
                    if self.bricklifes == 0:
                        print("solid brick disappear")
                        self.bricks.remove(brick)
                        self.ball.inverse_velocity_y()
                        self.gamepoints = self.gamepoints + 1

                        # print("collision ball with brick")
                        # self.bricks.remove(brick)
                        # self.ball.inverse_velocity_y()

    def handle_collision_with_pad(self, ball):
        if ball.collision(self.pad):
            print("collision ball with pad")
            self.ball.inverse_velocity_y()

            # def timer(self):
            #    self.start_ticks = pygame.time.get_ticks()  # starter tic
            #    while Game.loop:  # mainloop
            #        self.seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000
            #        if self.seconds > 10:
            #            break
            #        print(self.seconds)
