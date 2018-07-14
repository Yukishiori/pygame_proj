from game_object import GameObject
from frame_counter import FrameCounter
from Platform.Platform import Platform
import game_object
from renderers.animation import Animation

class PlatformSpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self, 0, 0)
        self.counter_continue = FrameCounter(20)
        self.counter_blank = FrameCounter(50)
        self.renderer = None
        self.is_spawning = True
        self.counter_blank.expired = True
        self.renderer = Animation(["images/bomb.png"], loop = True)


    def update(self):
        if self.counter_blank.expired:
            self.is_spawning = True
            # print('hello')
        else:
            self.is_spawning = False
            self.counter_blank.run()
            print(self.counter_blank.count)

        if self.is_spawning:
            self.counter_continue.run()
            if self.counter_continue.expired:
                self.spawn()
                self.counter_continue.reset()

    def spawn(self):
        platform = game_object.recycle(Platform, 1343, 650)
        platform.v_x = 3
