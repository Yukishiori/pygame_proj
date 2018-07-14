from menu.menu import Menu
from menu.start import Start
import game_object

class MenuScene:
    def __init__(self):
        pass
    def setup(self):
        menu = Menu(640,368)
        game_object.add(menu)

        start = Start(650, 450)
        game_object.add(start)
    def destroy(self):
        game_object.clear()

