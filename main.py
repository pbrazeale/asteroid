import pygame
from constants import *

def main():
    pygame.init()
    clock = pygame.time.clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick / 1000

    pygame.quit()


    print("Starting Asteroids!")
    print (f"Screen width: {constants.SCREEN_WIDTH}")
    print (f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()