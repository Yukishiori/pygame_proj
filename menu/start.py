from game_object import GameObject
from renderers.image_renderers import ImageRenderer
from scenes.scene_manager import global_scene_manager
from scenes.gameplay_scene import GameplayScene
from input.input_manager import global_input_manager

class Start(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self,x,y)
        self.renderer = ImageRenderer("menu/start.png")

    def update(self):
        GameObject.update(self)
        # if global_input_manager.x_pressed:
        #     gameplay = GameplayScene()
        #     global_scene_manager.change_scene(gameplay)
