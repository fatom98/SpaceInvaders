import pygame

from main.setup import BLACK, LASER_IMG


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = LASER_IMG.convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_y = -15

    def update(self):
        self.rect.centery += self.speed_y
