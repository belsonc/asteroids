#creation of asteroid class

from constants import *
import pygame
import random
from circleshape import CircleShape
#from asteroidfield import AsteroidField

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, asteroids):
        super().__init__(x, y, radius)
        self.asteroids_group = asteroids

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    #moving the asteroid
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self, asteroidfield, asteroids):
        old_radius = self.radius
        old_x = self.position.x
        old_y = self.position.y
        old_velocity = self.velocity

        pygame.sprite.Sprite.kill(self)
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20,50)
            other_new_angle = -new_angle
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            first_new_asteroid = Asteroid(old_x, old_y, new_radius)
            second_new_asteroid = Asteroid(old_x, old_y, new_radius)
            #first_new_asteroid.velocity = old_velocity
            #second_new_asteroid.velocity = old_velocity
            first_new_asteroid.velocity = old_velocity.rotate(new_angle) * 1.2
            second_new_asteroid.velocity = old_velocity.rotate(other_new_angle) * 1.2
            #asteroidfield.spawn(first_new_asteroid.radius, first_new_asteroid.position, first_new_asteroid.velocity)
            #asteroidfield.spawn(second_new_asteroid.radius, second_new_asteroid.position, second_new_asteroid.velocity)
            asteroids.add(first_new_asteroid)
            asteroids.add(second_new_asteroid)