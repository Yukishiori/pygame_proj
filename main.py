import pygame

from Platform.Platform import Platform
from player.player import Player

import game_object

from enemy.enemy_spawner import EnemySpawner
from Platform.platform_spawner import PlatformSpawner
from Platform.platform_flying_spawner import PlatformFlyingSpawner
from input.input_manager import InputManager

BG = (255, 255, 0)

# 1. Init pygame
pygame.init()

# 2. Set screen
SIZE = (1280, 690)
canvas = pygame.display.set_mode(SIZE)

# 3. Clock
clock = pygame.time.Clock()

loop = True

input_manager = InputManager()

player = Player(50, 0, input_manager)

game_object.add(player)

platform_spawner = PlatformSpawner()
game_object.add(platform_spawner)
enemy_spawner = EnemySpawner()
game_object.add(enemy_spawner)
platform_flying_spawner = PlatformFlyingSpawner()
game_object.add(platform_flying_spawner)


for i in range(21):
    platform2 = Platform(32 + i * 64, 650)
    game_object.add(platform2)



# for j in range(1):
#     platform_flying = PlatformFlying(32 + j * 64, 200)
#     game_object.add(platform_flying)






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

