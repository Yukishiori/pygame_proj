import pygame

from Platform.Platform import Platform
from player.player import Player

import game_object

from enemy.enemy_spawner import EnemySpawner
from input.input_manager import InputManager

BG = (255, 255, 0)

# 1. Init pygame
pygame.init()

# 2. Set screen
SIZE = (1280, 720)
canvas = pygame.display.set_mode(SIZE)

# 3. Clock
clock = pygame.time.Clock()

loop = True

input_manager = InputManager()

player = Player(50, 0, input_manager)

game_object.add(player)
game_object.add(EnemySpawner())

for i in range(15):
    platform2 = Platform(32 + i * 64, 600)
    game_object.add(platform2)

platform = Platform(300, 650)
game_object.add(platform)

platform = Platform(500, 500)
game_object.add(platform)

platform = Platform(64, 500)
game_object.add(platform)

platform = Platform(120, 400)
game_object.add(platform)

while loop:
    # 1. Event processing
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            input_manager.update(event)

    game_object.update()

    # 2. Draw
    canvas.fill(BG)

    game_object.render(canvas)

    pygame.display.set_caption('Micro game')

    # 3. Flip
    pygame.display.flip()
    clock.tick(60)
