import pygame
from physicsobject import RectangleObject
from config import player_speed, player_size, player_color, player_jump_speed

class Player(RectangleObject):
    def __init__(self, x, y, size=player_size, color=player_color):
        super().__init__(x, y, size, color)
        self.on_ground = False

    def move(self, dt, direction):
        self.rect.x += player_speed * dt * direction

    def jump(self):
        self.vel_y -= player_jump_speed
        self.on_ground = False

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move(dt, -1)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.move(dt, 1)

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

        self.apply_gravity(dt)
        self.check_floor_collision()

