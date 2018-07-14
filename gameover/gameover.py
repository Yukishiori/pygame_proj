from game_object import GameObject
from renderers.image_renderers import ImageRenderer

class Gameover(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer("gameover/gameover.png")