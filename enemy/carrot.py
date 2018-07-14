import pygame
from box_collider import BoxCollider
from frame_counter import FrameCounter
from game_object import GameObject
from renderers.animation import Animation


class Carrot(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.box_collider = BoxCollider(64,32)
        self.renderer = Animation(["images/carrot_animation/carrot1.png",
                                   "images/carrot_animation/carrot2.png",
                                   "images/carrot_animation/carrot3.png",
                                   "images/carrot_animation/carrot4.png",
                                   "images/carrot_animation/carrot5.png",
                                   "images/carrot_animation/carrot6.png"],loop = True)
        self.spawn_counter = FrameCounter(50)

    def update(self):
        GameObject.update(self)
        self.spawn_counter.run()
        if self.spawn_counter.expired:
            self.x -= 20
            self.deactivate_if_needed()
            # self.spawn_counter.reset()
        else:
            self.x -= 0

    def deactivate_if_needed(self):
        if self.x + 64 <0:
            self.spawn_counter.reset()
            self.deactivate()
