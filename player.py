import pygame
from rectangle import Rectangle
from config import player_speed, player_size, colors

class Player(Rectangle):
    def __init__(self, x, y):
        super().__init__(x, y, player_size, colors["BLUE"])  # Blue rectangle
        self.speed = player_speed

    def move(self, dt, direction):
        self.rect.x += self.speed * dt * direction

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.move(dt, -1)
        if keys[pygame.K_RIGHT]:
            self.move(dt, 1)

    #def draw(self, screen):
        #pygame.draw.rect(screen, colors["BLUE"], self.rect)