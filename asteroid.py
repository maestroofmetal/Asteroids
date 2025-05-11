import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
    #draw the asteroids
    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position,self.radius,2)

    def update(self, dt):
        self.position = self.position + self.velocity * dt

    def split(self, asteroids):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # set the velocities
            random_angle = random.uniform(20,50)
            velocity1 = self.velocity.rotate(random_angle) * 1.2
            velocity2 = self.velocity.rotate(-random_angle) * 1.2
             
            # Extract x and y from position vector
            x, y = self.position.x, self.position.y        
                     
            #create two new asteroids
            new_radius= self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(x, y ,new_radius)
            new_asteroid2 = Asteroid(x, y, new_radius)
            
            # Sets velocities
            new_asteroid1.velocity = velocity1
            new_asteroid2.velocity = velocity2
            #adds the new asteroids to the same groups
            asteroids.add(new_asteroid1, new_asteroid2)