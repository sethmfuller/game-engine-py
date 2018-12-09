# Name: Seth M. Fuller
# Date: 11/27/2018
# File: Scene.py

import pygame
import os


class Thing(pygame.sprite.Sprite):

    def __init__(self, scene, image_file, initial_x, initial_y):
        pygame.sprite.Sprite.__init__(self)

        self.scene = scene
        self.image = pygame.image.load(image_file)
        self.visible = True
        self.x = initial_x
        self.y = initial_y
        self.dx = 10
        self.dy = 1

        # Bounds actions
        self.LEAVE = 0
        self.BOUNCE = 1
        self.STOP = 2
        self.SKID = 3
        self.DIE = 4

        self.bounds_action = self.LEAVE

        self.scene.add_sprite(self)

    def update(self, *args):
        self.x += self.dx
        self.y += self.dy

        # draw image
        if self.visible:
            self.scene.screen.blit(self.image, (self.x, self.y))
            self.check_bounds()

    def set_bounds_action(self, action):
        self.bounds_action = action

    def check_bounds(self):
        if self.bounds_action == self.BOUNCE:
            if self.hits_left_or_right():
                self.dx = self.dx * -1
            if self.hits_top_or_bottom():
                self.dy = self.dy * -1

        if self.bounds_action == self.STOP:
            if self.hits_left_or_right():
                self.dx = 0
                self.dy = 0
            if self.hits_top_or_bottom():
                self.dx = 0
                self.dy = 0

        if self.bounds_action == self.SKID:
            if self.hits_left_or_right():
                self.dx = 0
            if self.hits_top_or_bottom():
                self.dy = 0

        if self.bounds_action == self.DIE:
            if self.hits_left_or_right() or self.hits_top_or_bottom():
                self.dx = 0
                self.dy = 0
                self.visible = False

    def hits_left_or_right(self):
        """Helper function used in check_bounds"""
        if self.x >= self.scene.screen.get_width() - self.image.get_width() or self.x <= 0:
            return True
        else: return False

    def hits_top_or_bottom(self):
        """Helper function used in check_bounds"""
        if self.y >= self.scene.screen.get_height() - self.image.get_height() or self.y <= 0:
            return True
        else: return False


    def set_position(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def change_x_by(self, change_amount):
        self.set_x(self.x + change_amount)

    def change_y_by(self, change_amount):
        self.set_y(self.y + change_amount)

    def set_dx(self, ndx):
        self.dx = ndx

    def set_dy(self, ndy):
        self.dy = ndy

    def change_dx_by(self, change_amount):
        self.set_dx(self.dx + change_amount)

    def change_dy_by(self, change_amount):
        self.set_dy(self.dy + change_amount)

    def change_image(self, image_location):
        self.image = pygame.image.load(image_location)

    def check_keys(self):
        """Check if keys are pressed down"""
