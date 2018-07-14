from game_object import GameObject
from renderers.image_renderers import ImageRenderer

class Menu(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer("menu/menu.png")