import pygame

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y, size, color):
        super().__init__()
        if isinstance(size, tuple):  # (width, height)
            width, height = size
        else:  # square
            width = height = size
            
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)