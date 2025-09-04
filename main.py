import pygame
from config import *
from player import Player
from platform import Platform

def main():
    print(f"Screen width: {screen_width}")
    print(f"Screen height: {screen_height}")

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Platformer Test")

    clock = pygame.time.Clock() # create a clock object
    dt = 0 # Delta time (time between frames)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # Adds all instances of the Player class to both groups
    Platform.containers = (drawable,)

    # Create player
    player = Player(60, screen_height - 200)

    # Create platforms
    platforms = pygame.sprite.Group()
    ground = Platform(0, screen_height - 40, (screen_width, 40))
    floating1 = Platform(120, screen_height - 170, (150, 20))
    floating2 = Platform(400, screen_height - 300, (200, 20))
    floating3 = Platform(840, screen_height - 300, (200, 20))
    platforms.add(ground, floating1, floating2, floating3)

    running = True
    while running:
        # checks if the user tries to exit the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(colors["BLACK"])

        # update
        updatable.update(dt)

        # Player-platform collisions
        player.check_platform_collision(platforms)

        # draw
        drawable.draw(screen) # draws game objects

        # tick
        dt = clock.tick(fps)/1000 # Limit FPS to 60
        pygame.display.flip() # refreshes the screen

    pygame.quit()

if __name__ == "__main__":
    main()