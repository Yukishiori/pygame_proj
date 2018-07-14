from game_object import GameObject
from frame_counter import FrameCounter
from enemy.carrot import Carrot
from enemy.warning_sign import WarningSign
import game_object
import random


class CarrotSpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self, 0, 0)
        self.image = None
        self.spawn_counter = FrameCounter(200)

    def update(self):
        self.spawn_counter.run()
        if self.spawn_counter.expired:
            ran_y = random.randint(200, 600)
            # print(warning_sign.x)
            game_object.recycle(WarningSign, 1200, ran_y)
            game_object.recycle(Carrot, 1365, ran_y)
            self.spawn_counter.reset()
