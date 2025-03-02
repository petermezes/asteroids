import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    group_asteroids = pygame.sprite.Group()
    group_shots = pygame.sprite.Group()

    Player.containers = (group_updatable, group_drawable)
    Asteroid.containers = (group_asteroids, group_updatable, group_drawable)
    AsteroidField.containers = group_updatable
    Shot.containers = (group_shots, group_updatable, group_drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        # loop head
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # loop body
        game_window.fill((0, 0, 0))

        group_updatable.update(dt)

        for group in group_drawable:
            group.draw(game_window)

        # check for collisions
        for asteroid in group_asteroids:
            if asteroid.collide(player):
                print("Game Over!")
                return
            for shot in group_shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()

        # kill shots that are off screen
        for shot in group_shots:
            if shot.position.x < 0 or shot.position.x > SCREEN_WIDTH or shot.position.y < 0 or shot.position.y > SCREEN_HEIGHT:
                shot.kill()

        # loop tail
        pygame.display.flip()
        dt = clock.tick(fps) / 1000


if __name__ == "__main__":
    main()
