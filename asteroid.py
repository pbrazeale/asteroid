from constants import *
from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius):
    
    def draw(x, y, radius):
        pygame.draw.circle(screen, (255,255,255), (x, y), radius, 2)

    def update(self, velocity, dt):
        self.move(self.position + self.velocity * dt)