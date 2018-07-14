from game_object import GameObject
from frame_counter import FrameCounter
from Platform.Platform import Platform
from enemy.spike_left import SpikeLeft
from enemy.spike_right import SpikeRight
import game_object
import random

class PlatformFlyingSpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self, 0, 0)
        self.counter = FrameCounter(130)
        self.image = None




    def update(self):
        self.counter.run()
        if self.counter.expired:

            self.spawn()
            # platform_flying = PlatformFlying(1343, 450)
            # game_object.add(platform_flying)
            self.counter.reset()

    def spawn(self):
        platform_speed = 5
        end_index = random.randint(4, 6)
        ran_y = random.randint(200,570)

        for i in range (end_index):
            if i == 0:
                spike = game_object.recycle(SpikeLeft, 1343 + i * 64 - 64 + 12, ran_y)
                spike.v_x = platform_speed
            if i == end_index - 1:
                spike = game_object.recycle(SpikeRight, 1343 + i * 64 - 12, ran_y)
                spike.v_x = platform_speed
            else:
                platform = game_object.recycle(Platform, 1343 + i*64, ran_y)
                platform.v_x = platform_speed


