import random

import pygame

from main.setup import WIDTH, HEIGHT, METEORS, BLACK


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(METEORS).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), -100)
        self.radius = int(self.rect.width * .85 / 2)
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(0, 10)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.bottom > HEIGHT or self.rect.left < 0 or self.rect.right > WIDTH:
            self.rect.center = (random.randint(0, WIDTH), -100)
