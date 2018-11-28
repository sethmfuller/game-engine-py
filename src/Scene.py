# Name: Seth M. Fuller
# Date: 11/27/2018
# File: Scene.py

import pygame
import sys

black = 0, 0, 0


class Scene:
    """Scene that encapsulates the animation background"""

    def __init__(self):
        self.size = self.width, self.height = 500, 300

        # The screen is similar to an html canvas in simpleGame.js
        self.screen = pygame.display.set_mode(self.size)
        self.sprites = []

    def update(self):
        pygame.display.flip()

    def clear(self):
        self.screen.fill(black)

    def set_size(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode(self.size)

    def start(self):
        pygame.init()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            self.clear()
            self.update()