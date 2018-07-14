from game_object import GameObject
from frame_counter import FrameCounter
from enemy.enemy import Enemy
import game_object


class EnemySpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self, 100, 0)
        self.counter = FrameCounter(120)
        self.image = None

    def update(self):
        self.counter.run()
        if self.counter.expired:
            self.spawn()
            # enemy = Enemy(100, 0)
            # game_object.add(enemy)
            self.counter.reset()
    def spawn(self):
        game_object.recycle(Enemy, 100, 0)