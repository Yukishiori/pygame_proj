from game_object import GameObject
from frame_counter import FrameCounter
from Platform.Platform import Platform
import game_object

class PlatformSpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self, 0, 0)
        self.counter = FrameCounter(20)
        self.image = None


    def update(self):
        self.counter.run()
        if self.counter.expired:
            self.spawn()
            self.counter.reset()

    def spawn(self):
        platform = game_object.recycle(Platform, 1343, 650)
        platform.v_x = 3

