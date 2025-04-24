import pygame
from player import *
from constants import *
from asteroid import * 
from asteroidfield import *
from shot import *
import sys


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #containers
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    #objects
    asteroidfield = AsteroidField()
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))

        for thing in drawable:
            thing.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            state = asteroid.collision(player)
            if state == True:
                print("Game over!")
                sys.exit()
            for bullet in shots:
                state = asteroid.collision(bullet)
                if state == True:
                    asteroid.split()
                    bullet.kill()



        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick / 1000

    pygame.quit()


    print("Starting Asteroids!")
    print (f"Screen width: {constants.SCREEN_WIDTH}")
    print (f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()