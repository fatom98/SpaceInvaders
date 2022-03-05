import os
import pygame

# GAME CONSTANTS
WIDTH, HEIGHT = 800, 1000
FPS = 60

# RGB COLORS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# IMAGES
pwd = os.getcwd()
assets_dir = os.path.join(pwd, "assets")
METEORS = [pygame.image.load(os.path.join(assets_dir, f"meteorBrown_{index}.png")) for index in range(1, 10)]
SHIP_IMG = pygame.image.load(os.path.join(assets_dir, "ship.png"))
BG_IMG = pygame.image.load(os.path.join(assets_dir, "bg.jpg"))
LASER_IMG = pygame.image.load(os.path.join(assets_dir, "laser.png"))
