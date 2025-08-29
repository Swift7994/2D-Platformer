import pygame
from config import *
from player import Player

def main():
    print(f"Screen width: {screen_width}")
    print(f"Screen height: {screen_height}")

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Test Window")

    clock = pygame.time.Clock() # create a clock object
    dt = 0 # Delta time (time between frames)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable) # Adds all instances of the Player class to both groups

    # Create player
    player = Player(100, screen_height - 100)

    print(f"debug: {drawable.sprites()}")

    running = True
    while running:
        # checks if the user tries to exit the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update
        updatable.update(dt)

        # draw
        screen.fill(colors["BLACK"])
        drawable.draw(screen) # draws game objects

        # tick
        dt = clock.tick(fps)/1000 # Limit FPS to 60
        pygame.display.flip() # refreshes the screen

    pygame.quit()

if __name__ == "__main__":
    main()