import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Creates groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group= pygame.sprite.Group()

    # sets containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers= (updatable, drawable, shots_group)
    
    # allows Asteroid Field to be called and spawn asteroids
    asteroid_field = AsteroidField()
    
    # sets delta time
    dt = 0   
    
    #draws the player     
    player = Player(SCREEN_WIDTH /2, SCREEN_WIDTH /2)
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        # makes the screen black
        screen.fill("black")
        
        # draws the player
        updatable.update(dt)
        
        for drawn in drawable:
            drawn.draw(screen)
        
        pygame.display.flip()
        
        #sets the frame rate to 60 fps
        dt = clock.tick(60)/1000
        
        
        # Adds collision detection
        for asteroid in asteroids:
            if player.collide(asteroid):
                sys.exit("Game over!")
                
        for asteroid in asteroids:
            for shot in shots_group:
                if shot is not None:
                    if shot.collide(asteroid):
                        asteroid.split(asteroids)
                        shot.kill()
                
                
        # shoots
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            shot = player.shoot()
            if shot is not None:
                shots_group.add(shot)
if __name__ == "__main__":
    main()