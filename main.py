import pygame

import game_object
from input.input_manager import global_input_manager

from scenes.gameover_scene import GameoverScene
from scenes.scene_manager import global_scene_manager
from scenes.menu_scene import MenuScene


from input.input_manager import InputManager


BG = (0, 0, 0)


def make_font(fonts, size):
    available = pygame.font.get_fonts()
    choices = map(lambda x: x.lower().replace(' ', ''), fonts)
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)


_cached_fonts = {}


def get_font(font_preferences, size):
    global _cached_fonts
    key = str(font_preferences) + '|' + str(size)
    font = _cached_fonts.get(key, None)
    if font == None:
        font = make_font(font_preferences, size)
        _cached_fonts[key] = font
    return font


_cached_text = {}


def create_text(text, fonts, size, color):
    global _cached_text
    key = '|'.join(map(str, (fonts, size, color, text)))
    image = _cached_text.get(key, None)
    if image == None:
        font = get_font(fonts, size)
        image = font.render(text, True, color)
        _cached_text[key] = image
    return image


# 1. Init pygame
pygame.init()

# warning_sound = pygame.mixer.Sound()

pygame.mixer.music.load("music/backgroundpygame.wav")
pygame.mixer.music.play(-1)

# 2. Set screen
SIZE = (1280, 690)
canvas = pygame.display.set_mode(SIZE)

# 3. Clock
clock = pygame.time.Clock()

loop = True

menu_scene = MenuScene()
global_scene_manager.change_scene(menu_scene)


# game_object.recycle(WarningSign, 1200, 0)
# game_object.add( background)



font_preferences = [
        "Bizarre-Ass Font Sans Serif",
        "They definitely dont have this installed Gothic",
        "Papyrus",
        "Comic Sans MS"]


while loop:
    # 1. Event processing
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            global_input_manager.update(event)

    # text1 = create_text("Score:", font_preferences, 28, (40, 128, 0))
    # text2 = create_text(str(game_object.score), font_preferences, 28, (40, 128, 0))

    game_object.update()

    # 2. Draw
    canvas.fill(BG)

    game_object.render(canvas)
    # background.renderer.render(canvas, background.x, background.y)

    if not type (global_scene_manager.current_scene) == GameoverScene:
        text1 = create_text("Score:", font_preferences, 28, (255, 0, 0))
        text2 = create_text(str(game_object.score), font_preferences, 28, (255, 0, 0))
        canvas.blit(text1,
            (105 - text1.get_width() // 2, 40 - text1.get_height() // 2))
        canvas.blit(text2,
                    (200 - text2.get_width() // 2, 40 - text2.get_height() // 2))
    else:
        text1 = create_text("Score:", font_preferences, 72, (40, 128, 0))
        text2 = create_text(str(game_object.score), font_preferences, 72, (40, 128, 0))
        canvas.blit(text1,
                    (640 - text1.get_width() // 2, 650 - text1.get_height() // 2))
        canvas.blit(text2,
                    (900 - text2.get_width() // 2, 650 - text2.get_height() // 2))
    pygame.display.set_caption('jump jump jump')

    # 3. Flip
    pygame.display.flip()
    clock.tick(60)

