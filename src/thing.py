# Name: Seth M. Fuller
# Date: 11/27/2018
# File: Scene.py

import pygame
import os


class Thing(pygame.sprite.Sprite):

    def __init__(self, scene, image_file, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.scene = scene

        self.image = pygame.Surface([width, height])
        self.image.blit(pygame.image.load(os.path.join('data', image_file)))

        # Add Surface to scene
        self.scene.blit(self.image)

