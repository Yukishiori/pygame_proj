import pygame
from gameover.gameover import Gameover
# from gameover.play_again import PlayAgain
import game_object


class GameoverScene:
    def __init__(self):
        pygame.mixer.Channel(0).play(pygame.mixer.Sound("music/game_over_sound.wav"))

    def setup(self):
        gameover = Gameover(640,368)
        game_object.add(gameover)

        # play_again = PlayAgain(640, 520)
        # game_object.add(play_again)

    def destroy(self):
        game_object.clear()