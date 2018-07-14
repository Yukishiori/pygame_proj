import pygame
from box_collider import BoxCollider
from frame_counter import FrameCounter
from game_object import GameObject

class Carrot(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("images/carrot.png")
        self.box_collider = BoxCollider(64,32)
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
