import pygame
from menu.menu import Menu
from menu.start import Start
import game_object

class MenuScene:
    def __init__(self):
        pygame.mixer.Channel(0).play(pygame.mixer.Sound("music/backgroundpygame.wav"))
    def setup(self):
        menu = Menu(640,368)
        game_object.add(menu)

        start = Start(650, 450)
        game_object.add(start)
    def destroy(self):
        game_object.clear()

