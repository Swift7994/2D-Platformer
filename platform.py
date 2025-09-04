import pygame
from physicsobject import RectangleObject
from config import colors

class Platform(RectangleObject):
    def __init__(self, x, y, size, color=colors["WHITE"]):
        super().__init__(x, y, size, color)

    def update(self, dt):
        pass

