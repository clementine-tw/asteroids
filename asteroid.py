import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            2
        )
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # calculates the velocity and radius of the 2 new asteroids
        random_angle = random.uniform(20, 50)
        first_velocity = self.velocity.rotate(random_angle)
        second_velocity = self.velocity.rotate(-random_angle)
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS

        # creates 2 new asteroids and makes them move faster
        first_asteroid = Asteroid(self.position.x, self.position.y, smaller_radius)
        first_asteroid.velocity = first_velocity * 1.2
        second_asteroid = Asteroid(self.position.x, self.position.y, smaller_radius)
        second_asteroid.velocity = second_velocity * 1.2

