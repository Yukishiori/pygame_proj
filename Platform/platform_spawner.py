from game_object import GameObject
from Platform.Platform import Platform
import game_object
import random

class PlatformSpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self, 0, 0)
        self.random_number = random.randint(0, 300)

    def update(self):
        # if self.x <0:
        game_object.recycle(Platform, 1343, 650)

