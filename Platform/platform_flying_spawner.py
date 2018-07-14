from game_object import GameObject
from frame_counter import FrameCounter
from Platform.Platform import Platform
from enemy.spike import Spike
import game_object
import random

class PlatformFlyingSpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self, 0, 0)
        self.counter = FrameCounter(150)
        self.image = None




    def update(self):
        self.counter.run()
        if self.counter.expired:

            self.spawn()
            # platform_flying = PlatformFlying(1343, 450)
            # game_object.add(platform_flying)
            self.counter.reset()

    def spawn(self):
        platform_speed = 6
        end_index = random.randint(5, 7)
        ran_y = random.randint(100, 550)

        for i in range (end_index):
            if i == 0 or i == end_index - 1:
                spike = game_object.recycle(Spike, 1343 + i*64, ran_y)
                spike.v_x = platform_speed
            else:
                platform = game_object.recycle(Platform, 1343 + i*64, ran_y)
                platform.v_x = platform_speed


