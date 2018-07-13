import pygame

import pygame
from box_collider import BoxCollider
from game_object import GameObject
import game_object


class PlatformFlying(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("images/map/forest.png")
        self.box_collider = BoxCollider(64, 64)

    # def run(self):
    #     self.x -= 3

    def update(self):
        GameObject.update(self)
        self.x -= 60

        self.deactivate_if_needed()
            # game_object.recycle(Platform, 1343, 600)

    def deactivate_if_needed(self):
        if self.x<0:
            self.deactivate()