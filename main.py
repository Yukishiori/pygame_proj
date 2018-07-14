import pygame

from Platform.Platform import Platform
from player.player import Player

import game_object
from game_event import GameEvent
from input.input_manager import InputManager


BG = (0, 0, 0)


def make_font(fonts, size):
    available = pygame.font.get_fonts()
    # get_fonts() returns a list of lowercase spaceless font names
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


# font = pygame.font.SysFont("my_game.ttf", 30)
#
# text = font.render("Hello, Usagi - chan!", True, (255, 250, 250))

font_preferences = [
        "Bizarre-Ass Font Sans Serif",
        "They definitely dont have this installed Gothic",
        "Papyrus",
        "Comic Sans MS"]

input_manager = InputManager()

player = Player(50, 400, input_manager)

game_object.add(player)
# game_object.recycle(WarningSign, 1200, 0)

game_event = GameEvent()
game_object.add(game_event)

for i in range(22):
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

    text1 = create_text("Score", font_preferences, 28, (40, 128, 0))
    text2 = create_text(str(game_object.score), font_preferences, 28, (40, 128, 0))

    game_object.update()

    # 2. Draw
    canvas.fill(BG)

    game_object.render(canvas)

    canvas.blit(text1,
        (105 - text1.get_width() // 2, 40 - text1.get_height() // 2))
    canvas.blit(text2,
                (200 - text2.get_width() // 2, 40 - text2.get_height() // 2))

    pygame.display.set_caption('Micro game')

    # 3. Flip
    pygame.display.flip()
    clock.tick(60)

