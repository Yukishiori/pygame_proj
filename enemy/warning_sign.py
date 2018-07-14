import pygame
from box_collider import BoxCollider
from frame_counter import FrameCounter
from game_object import GameObject
from renderers.animation import Animation

class WarningSign(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = Animation(["images/warning_sign.png"], loop = True)
        self.box_collider = BoxCollider(64,64)
        self.count = FrameCounter(50)
        pygame.mixer.Channel(3).play(pygame.mixer.Sound("music/warning (1).wav"))

    def update(self):
        GameObject.update(self)
        # self.x = 1000

        self.count.run()
        if self.count.expired:
            self.deactivate_if_needed()
            self.count.reset()

    def deactivate_if_needed(self):
        self.deactivate()