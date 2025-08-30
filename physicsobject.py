import pygame
from config import gravity

class PhysicsObject(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        if isinstance(size, tuple):  # (width, height)
            width, height = size
        else:  # square
            width = height = size

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft = (x, y))

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

class RectangleObject(PhysicsObject):
    def __init__(self, x, y, size, color):
        super().__init__(x, y, size)
        pygame.draw.rect(self.image, color, self.image.get_rect())

class CircleObject(PhysicsObject):
    def __init__(self, x, y, radius, color):
        # Create a square surface for the circle (diameter = radius*2)
        super().__init__(x, y, (radius*2, radius*2))

        pygame.draw.circle(
            self.image, 
            color, 
            (radius, radius),  # center of the local surface
            radius
)