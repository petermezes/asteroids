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

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        # loop head
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # loop body
        pygame.Surface.fill(game_window, (0, 0, 0))
        player.draw(game_window)
        player.update(dt)

        # loop tail
        pygame.display.flip()
        dt = clock.tick(fps) / 1000


if __name__ == "__main__":
    main()
