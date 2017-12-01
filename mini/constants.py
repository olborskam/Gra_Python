import json

SCREEN_SIZE = (800, 600)
SCREEN_WIDTH = SCREEN_SIZE[0]
SCREEN_HEIGHT = SCREEN_SIZE[1]

SCREEN_NAME = "Super arkanoid"

GAME_TICK_TIME = 30
MENU_TICK_TIME = 0.3 * GAME_TICK_TIME

BALL_VELOCITY = 10

PAD_VELOCITY = 20

X_BUTTON_OFFSET = 50
Y_BUTTON_OFFSET = 50
Y_BUTTONS_INTERVAL = 100

def load_lifes_from_json():
    file = json.load(open("resources/settings.json"))
    return file["lifes"]
