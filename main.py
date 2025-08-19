import pygame
from config import screen_width, screen_height

def main():
    print(f"Screen width: {screen_width}")
    print(f"Screen height: {screen_height}")

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Test Window")

    clock = pygame.time.Clock() # create a clock object
    # dt = 0 # Delta time (time between frames)

    running = True
    while running:
        # checks if the user tries to exit the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60)/1000 # Limit FPS to 60 and calculate delta time
        pygame.display.flip() # refreshes the screen

    pygame.quit()

if __name__ == "__main__":
    main()