import pygame

from main.setup import WIDTH, HEIGHT, FPS, BLACK, BG_IMG
from sprites.mob import Mob
from sprites.player import Player

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")


class Game:
    def __init__(self, win):
        self.win = win
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.mob_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.player = None
        self.initialize()

    def main(self):
        running = True
        while running:
            # time management
            self.clock.tick(FPS)
            # manage inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                pressed = pygame.key.get_pressed()

                if pressed[pygame.K_SPACE]:
                    bullet = self.player.shoot()
                    self.all_sprites.add(bullet)
                    self.bullet_sprites.add(bullet)

                if pressed[pygame.K_RIGHT]:
                    self.player.set_speed(10)
                elif pressed[pygame.K_LEFT]:
                    self.player.set_speed(-10)
                else:
                    self.player.set_speed(0)
            # update
            self.all_sprites.update()
            # collision
            impact = pygame.sprite.spritecollide(self.player, self.mob_sprites, False, pygame.sprite.collide_circle)
            if impact:
                running = False
            if hits := pygame.sprite.groupcollide(self.bullet_sprites, self.mob_sprites, True, True, pygame.sprite.collide_circle):
                for _ in hits:
                    m = Mob()
                    self.all_sprites.add(m)
                    self.mob_sprites.add(m)
            # draw
            self.win.fill(BLACK)
            self.win.blit(BG_IMG, (0, 0))
            self.all_sprites.draw(self.win)
            pygame.display.update()

    def initialize(self):
        self.player = Player()
        self.all_sprites.add(self.player)

        for _ in range(30):
            m = Mob()
            self.all_sprites.add(m)
            self.mob_sprites.add(m)


if __name__ == "__main__":
    game = Game(window)
    game.main()
