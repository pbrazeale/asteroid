from constants import *
from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new1_vector = self.velocity.rotate(angle)
            new2_vector = self.velocity.rotate(angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new1 = Asteroid(self.position, self.position, new_radius)
            new2 = Asteroid(self.position, self.position, new_radius)
            new1.velocity = new1_vector * 1.2
            new2.velocity = new2_vector * 1.2
