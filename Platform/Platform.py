import pygame

import pygame
from box_collider import BoxCollider
from game_object import GameObject
import game_object
from renderers.animation import Animation



class Platform(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)

        self.box_collider = BoxCollider(64, 64)
        self.v_x = game_object.game_speed #velocity
        self.renderer = Animation(["images/map/forest.png"],loop = True)

    def update(self):
        GameObject.update(self)
        self.x -= self.v_x

        self.deactivate_if_needed()


    def deactivate_if_needed(self):
        if self.x + 64 <0:
            self.deactivate()