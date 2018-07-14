from game_object import GameObject
from renderers.animation import Animation

class PlayerDies(GameObject):
    def __init__ (sefl, x, y, self):
        GameObject.__init__(self,x,y)
        self.renderer = Animation(["images/player_dies/sprite-0003.png",
                                   "images/player_dies/sprite-0004.png",
                                   "images/player_dies/sprite-0005.png",
                                   "images/player_dies/sprite-0006.png",
                                   "images/player_dies/sprite-0007.png",
                                   "images/player_dies/sprite-0008.png",
                                   "images/player_dies/sprite-0009.png",
                                    "images/player_dies/sprite-00010.png",], loop = True)
