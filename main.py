import pygame
from player import *
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.draw(screen)

        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick / 1000

    pygame.quit()


    print("Starting Asteroids!")
    print (f"Screen width: {constants.SCREEN_WIDTH}")
    print (f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()