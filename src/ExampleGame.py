# Author: Seth Fuller
# Date: 11/27/2018
# File: ExampleGame.py

from src.Scene import Scene
from src.Thing import Thing
import pygame
from pygame.locals import *


def main():
    scene = Scene()
    scene.set_size(800, 500)

    sprite3 = Thing(scene, "../assets/MaceBall.png", 100, 0)
    sprite3.set_dx(0)
    sprite3.set_dy(10)
    sprite3.set_bounds_action(sprite3.BOUNCE)

    sprite4 = Thing(scene, "../assets/MaceBall.png", 200, 400)
    sprite4.set_dx(0)
    sprite4.set_dy(-10)
    sprite4.set_bounds_action(sprite4.BOUNCE)

    sprite5 = Thing(scene, "../assets/MaceBall.png", 300, 0)
    sprite5.set_dx(0)
    sprite5.set_dy(10)
    sprite5.set_bounds_action(sprite5.BOUNCE)

    sprite1 = Thing(scene, "../assets/MaceBall.png", 400, 400)
    sprite1.set_dx(0)
    sprite1.set_dy(-10)
    sprite1.set_bounds_action(sprite1.BOUNCE)

    sprite2 = Thing(scene, "../assets/MaceBall.png", 500, 0)
    sprite2.set_dx(0)
    sprite2.set_dy(-10)
    sprite2.set_bounds_action(sprite2.BOUNCE)

    sprite6 = Thing(scene, "../assets/MaceBall.png", 600, 400)
    sprite6.set_dx(0)
    sprite6.set_dy(10)
    sprite6.set_bounds_action(sprite6.BOUNCE)

    player = Player(scene, "../assets/joint.png", 100, 0)
    player.set_bounds_action(player.BOUNCE)

    scene.start()


class Player(Thing):

    def __init__(self, scene, image_file, initial_x, initial_y):
        Thing.__init__(self, scene, image_file, initial_x, initial_y)

    def check_keys(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == pygame.K_UP:
                self.set_dy(-10)
            if event.type == KEYUP and event.key == pygame.K_UP:
                self.set_dy(0)
            if event.type == KEYDOWN and event.key == pygame.K_DOWN:
                self.set_dy(10)
            if event.type == KEYUP and event.key == pygame.K_DOWN:
                self.set_dy(0)
            if event.type == KEYDOWN and event.key == pygame.K_RIGHT:
                self.set_dx(10)
            if event.type == KEYUP and event.key == pygame.K_RIGHT:
                self.set_dx(0)
            if event.type == KEYDOWN and event.key == pygame.K_LEFT:
                self.set_dx(-10)
            if event.type == KEYUP and event.key == pygame.K_LEFT:
                self.set_dx(0)

    def check_collisions(self):
        self.collides_with(self)


if __name__ == '__main__':
    while main():
        pass
