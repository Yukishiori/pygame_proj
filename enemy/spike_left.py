import pygame

import pygame
from box_collider import BoxCollider
from game_object import GameObject
import game_object
from renderers.animation import Animation


class SpikeLeft(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = Animation(["enemy/left.png"], loop=True)
        self.box_collider = BoxCollider(10, 60)
        self.v_x = game_object.game_speed #velocity

    def update(self):
        GameObject.update(self)
        self.x -= self.v_x
        self.deactivate_if_needed()


    def deactivate_if_needed(self):
        if self.x + 64 <0:
            self.deactivate()
