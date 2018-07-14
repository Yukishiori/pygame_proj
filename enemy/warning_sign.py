import pygame
from box_collider import BoxCollider
from frame_counter import FrameCounter
from game_object import GameObject

class WarningSign(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("images/warning.png")
        self.box_collider = BoxCollider(64,64)
        self.count = FrameCounter(50)
        # pygame.mixer.music.load('music/warning.wav')
        # pygame.mixer.music.play(0)

    def update(self):
        GameObject.update(self)
        # self.x = 1000

        self.count.run()
        if self.count.expired:
            self.deactivate_if_needed()
            self.count.reset()

    def deactivate_if_needed(self):
        self.deactivate()