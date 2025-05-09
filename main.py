import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0   
    
    #draws the player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2        
    player = Player(x, y)
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        # makes the screen black
        screen.fill("black")
        
        # draws the player
        player.update(dt)
        player.draw(screen)
        
        #sets the frame rate to 60 fps
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()