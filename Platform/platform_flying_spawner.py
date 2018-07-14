from game_object import GameObject
from frame_counter import FrameCounter
from Platform.platform_flying import PlatformFlying
import game_object

class PlatformFlyingSpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self, 0, 0)
        self.counter = FrameCounter(20)


    def update(self):
        self.counter.run()
        if self.counter.expired:
            platform_flying = PlatformFlying(1343, 450)
            game_object.add(platform_flying)
            self.counter.reset()
        # game_object.recycle(PlatformFlying, 1343, 200)
