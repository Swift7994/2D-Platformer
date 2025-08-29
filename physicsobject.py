import pygame
from config import gravity

class PhysicsObject(pygame.sprite.Sprite):
    def __init__(self, x, y, size, color):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        if isinstance(size, tuple):  # (width, height)
            width, height = size
        else:  # square
            width = height = size
            
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.vel_x = 0  # horizontal velocity
        self.vel_y = 0  # vertical velocity
        self.gravity = gravity

    def apply_gravity(self, dt):
        self.vel_y += self.gravity * dt
        self.rect.y += self.vel_y * dt
        
    # Temporary floor collision
    def check_floor_collision(self):
        if self.rect.bottom >= 500:
            self.rect.bottom = 500
            self.vel_y = 0
            self.on_ground = True
