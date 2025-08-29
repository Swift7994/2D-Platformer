import pygame
from rectangle import Rectangle
from config import player_speed, player_size, player_color, jump_speed

class Player(Rectangle):
    def __init__(self, x, y):
        super().__init__(x, y, player_size, player_color)
        self.speed = player_speed
        self.jump_speed = jump_speed
        self.vel_y = 0
        self.on_ground = False

    def move(self, dt, direction):
        self.rect.x += self.speed * dt * direction

    def jump(self):
        self.vel_y = self.jump_speed
        self.on_ground = False

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move(dt, -1)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.move(dt, 1)

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()
        # apply gravity

