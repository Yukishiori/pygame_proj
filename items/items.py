import pygame
from box_collider import BoxCollider
from game_object import GameObject
import random

class Items(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        rnd = random.randint(1,3)
        if rnd == 1:
            self.image = pygame.image.load("images/banana.png")
        if rnd == 2:
            self.image = pygame.image.load("images/pizza.png")
        if rnd == 3:
            self.image = pygame.image.load("images/fish.png")

        self.box_collider = BoxCollider(64,64)

    def update(self):
        GameObject.update(self)
        self.x -= 3
        self.deactivate_if_needed()

    def deactivate_if_needed(self):
        if self.x + 64<0:
            self.deactivate()