from renderers.animation import Animation
from game_object import GameObject

class Background(GameObject):
    def __init__ (self,x,y):
        GameObject.__init__(self,x,y)
        self.renderer = Animation(["images/background.png"], loop = True)

