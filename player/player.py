import numpy
import pygame

from Platform.Platform import Platform
from enemy.spike_left import SpikeLeft
from enemy.spike_right import SpikeRight
from enemy.carrot import Carrot
from items.items import Items
from box_collider import BoxCollider
import game_object
from game_object import GameObject
from game_object import collide_with, add as add_game_object
from frame_counter import FrameCounter
from renderers.player_animator import PlayerAnimator
from scenes.scene_manager import global_scene_manager
from scenes.gameover_scene import GameoverScene
from input.input_manager import global_input_manager
from player.player_dies import PlayerDies

class Player(GameObject):
    # 1. Create constructor (properties)
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.shoot_lock = False
        self.counter = FrameCounter(30)
        self.box_collider = BoxCollider(64, 128)
        self.dx = 0
        self.dy = 0
        self.jump_speed = -17
        self.renderer = PlayerAnimator()



    # 2. Describe action / method / behavior
    def update(self):
        GameObject.update(self)
        self.move()
        # self.shoot()
        self.deactivate_if_need()
        self.update_animator()

    def update_animator(self):
        self.renderer.update(self.dx,self.dy)

        collide_list2 = collide_with(self.box_collider, Items)
        for obj in collide_list2:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("music/eating_fish_pizza_coin.wav"))
            obj.deactivate()
            game_object.score += 10

        game_object.score += 1


    def move(self):
        self.dx = 0
        # self.dy = 0
        if global_input_manager.right_pressed:
            self.dx += 3
        if global_input_manager.left_pressed:
            self.dx -= 7
        if global_input_manager.up_pressed:
            box_at_bottom = self.box_collider
            box_at_bottom.y = self.box_collider.y + 2
            btm = game_object.collide_with(box_at_bottom, Platform)
            for obj in btm:
                if type(obj) == Platform:
                    self.dy = self.jump_speed
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound("music/jumping.wav"))

        self.dy += 0.5

        self.check_future_y()
        self.check_future_x()
        # print(self.dx)

    def check_future_y(self):
        future_box = BoxCollider(64, 120)
        future_box.x = self.x
        future_box.y = self.y
        # future_box.x += self.dx
        future_box.y += self.dy

        collided_list = game_object.collide_with(future_box, Platform)
        for obj in collided_list:
            if type(obj) == Platform:
                move_continue = True
                distance = 1
                while move_continue:
                    box = self.box_collider
                    box.y += distance
                    collided_list2 = game_object.collide_with(box, Platform)
                    for obj in collided_list2:
                        if type(obj) == Platform:
                            move_continue = False
                        else:
                            distance += 1
                            self.y += numpy.sign(self.dy)
                self.dy = 0
        self.y += self.dy

    def check_future_x(self):
        future_box = BoxCollider(64, 120)
        future_box.x = self.x
        future_box.y = self.y

        # future_box.x += self.dx
        future_box.x += self.dx

        collided_list = game_object.collide_with(future_box, Platform)
        for obj in collided_list:
            if type(obj) == Platform:
                # print('hello')
                self.dx = 0

        self.x += self.dx

    def deactivate_if_need(self):
        collided_with1 = game_object.collide_with(self.box_collider, SpikeLeft)
        if len(collided_with1) > 0:
            self.deactivate()
        if self.y > 700:
            self.deactivate()

        collided_with2 = game_object.collide_with(self.box_collider, SpikeRight)
        if len(collided_with2) > 0:
            self.deactivate()

        collided_with3 = game_object.collide_with(self.box_collider, Carrot)
        if len(collided_with3) > 0:
            self.deactivate()

    def deactivate(self):
        GameObject.deactivate(self)
        death = PlayerDies(self.x, self.y)
        add_game_object(death)
        over = GameoverScene()
        global_scene_manager.change_scene(over)

