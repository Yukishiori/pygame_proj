import game_object
from Platform.platform_flying_spawner import PlatformFlyingSpawner
from Platform.platform_spawner import PlatformSpawner
from enemy.carrot_spawner import CarrotSpawner
from items.items_spawner import ItemsSpawner
from frame_counter import FrameCounter
import random

class GameEvent(game_object.GameObject):

    def __init__(self):
        game_object.GameObject.__init__(self, 0, 0)
        self.delay = FrameCounter(random.randint(100, 200))

        self.platform_spawner = PlatformSpawner()
        game_object.add(self.platform_spawner)

        self.platform_flying_spawner = PlatformFlyingSpawner()
        game_object.add(self.platform_flying_spawner)
        self.platform_flying_spawner.counter.expired = True

        self.carrot_spawner = CarrotSpawner()
        game_object.add(self.carrot_spawner)

        self.items_spawner = ItemsSpawner()
        game_object.add(self.items_spawner)

    def update(self):



        self.delay.run()
        if self.delay.expired:
            self.platform_spawner.counter_blank.reset()
            self.platform_flying_spawner.counter.reset()
            self.delay.reset()

