from game_object import GameObject
from frame_counter import FrameCounter
from enemy.carrot import Carrot
import game_object
import random


class CarrotSpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self, 0, 0)
        self.counter = FrameCounter(150)
        self.image = None

    def update(self):
        self.counter.run()
        if self.counter.expired:
            self.spawn()
            # enemy = Enemy(100, 0)
            # game_object.add(enemy)
            self.counter.reset()

    def spawn(self):
        ran_y = random.randint(200, 600)
        game_object.recycle(Carrot,1343,ran_y)