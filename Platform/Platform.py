import pygame

from box_collider import BoxCollider
from game_object import GameObject


class Platform(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("images/blood_cells/blood-cell1.png")
        self.box_collider = BoxCollider(64, 64)


    def update(self):
        GameObject.update(self)
        # self.y += 3
