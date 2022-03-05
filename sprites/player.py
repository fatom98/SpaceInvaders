import pygame

from main.setup import HEIGHT, WIDTH, SHIP_IMG, BLACK, RED
from sprites.bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(SHIP_IMG.convert(), (49, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 50)
        self.radius = 20
        self.speed_x = 0

    def update(self):
        self.rect.centerx += self.speed_x
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIDTH)

    def set_speed(self, speed_x):
        self.speed_x = speed_x

    def shoot(self) -> Bullet:
        return Bullet(self.rect.centerx, self.rect.top)
