from game_object import GameObject
from renderers.image_renderers import ImageRenderer
from input.input_manager import global_input_manager
# import game_object
# from scenes.gameplay_scene import GameplayScene
from scenes.menu_scene import MenuScene
from scenes.scene_manager import global_scene_manager


class Gameover(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer("gameover/gameover.png")

    def update(self):
        if global_input_manager.x_pressed:
            # gameplay_scene = GameplayScene()
            pass
            # global_scene_manager.change_scene(gameplay_scene)
            # menu = MenuScene()
            # global_scene_manager.change_scene(menu)