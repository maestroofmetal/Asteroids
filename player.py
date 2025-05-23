from circleshape import *
from constants import *
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
  
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
    def rotate(self, dt):
        turn_amount = PLAYER_TURN_SPEED * dt
        self.rotation += turn_amount
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt
  
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        if self.timer <= 0:
			# creates the shot 
            shot = Shot(self.position)
			# sets the shot's velocity
            velocity = pygame.Vector2(0,1)
            velocity.rotate_ip(self.rotation)
            velocity *= PLAYER_SHOOT_SPEED
            shot.velocity = velocity
            # reset the cooldown timer
            self.timer = PLAYER_SHOOT_COOLDOWN
            return shot