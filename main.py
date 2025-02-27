import pygame
from constants import *
from player import Player

game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
fps = 60


def init_log():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


def main():
    init_log()
    pygame.init()

    dt = 0

    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()

    Player.containers = (group_updatable, group_drawable)
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # loop head
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # loop body
        group_updatable.update(dt)

        game_window.fill((0, 0, 0))

        for group in group_updatable:
            group.draw(game_window)

        # loop tail
        pygame.display.flip()
        dt = clock.tick(fps) / 1000


if __name__ == "__main__":
    main()
