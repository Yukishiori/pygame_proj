from game_object import GameObject
from frame_counter import FrameCounter
from Platform.Platform import Platform
from enemy.obstacle import Obstacle
import game_object
import random

class PlatformFlyingSpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self, 0, 0)
        self.counter = FrameCounter(300)
        self.image = None


    def update(self):
        self.counter.run()
        if self.counter.expired:
            self.spawn()
            # platform_flying = PlatformFlying(1343, 450)
            # game_object.add(platform_flying)
            self.counter.reset()

    def spawn(self):
        # self.rand.x = random.randint()
        # for a in range(2):
        #     Obstacle(32 + a * 64, 650)
        #     for j in range(2):
        #         Platform(32 + j * 64, 650)


        platform = game_object.recycle(Platform, 1343, 450)
        obstacle = game_object.recycle(Obstacle,)
        platform.v_x = 6
