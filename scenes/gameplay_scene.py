import pygame
from Platform.Platform import Platform
from background.background import Background
from player.player import Player
from game_event import GameEvent
from renderers.animation import Animation
import game_object

class GameplayScene:
    def __init__(self):
        pass

    def setup(self):
        player = Player(50, 400)

        game_object.add(player)

        game_event = GameEvent()
        game_object.add(game_event)
        background = Background(640, 320)
        game_object.game_objects.insert(0, background)


        for i in range(22):
            platform2 = Platform(32 + i * 64, 650)
            game_object.add(platform2)

    def destroy(self):
        game_object.clear()

