# Name: Seth M. Fuller
# Date: 11/27/2018
# File: Scene.py

import pygame
import sys


class Scene:
    """Scene that encapsulates the animation background"""

    def __init__(self):
        self.size = self.width, self.height = 500, 300

        # The screen is similar to an html canvas in simpleGame.js
        self.screen = pygame.display.set_mode(self.size)
        self.background_color = (255, 255, 255)
        self.sprites = []

    def update(self):
        pygame.display.flip()
        pygame.display.get_surface().fill(self.background_color)

        for sprite in self.sprites:
            sprite.update()

    def set_size(self, width, height):
        """Set the size of the Scene"""

        self.width = width
        self.height = height
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)

    def set_color(self, color):
        """Set the background color of the scene"""
        self.background_color = color

    def add_sprite(self, sprite):
        """Add Sprite to scene so that it can be rendered and updated"""
        self.sprites.append(sprite)

    def start(self):
        pygame.init()

        # Game Loop
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            self.update()
