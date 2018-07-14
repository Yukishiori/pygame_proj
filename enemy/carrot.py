import pygame
from box_collider import BoxCollider
from game_object import GameObject

class Carrot(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("images/carrot.png")
        self.box_collider = BoxCollider(64,32)

    def update(self):
        GameObject.update(self)
        self.x -= 20
        self.deactivate_if_needed()

    def deactivate_if_needed(self):
        if self.x + 64 <0:
            self.deactivate()
