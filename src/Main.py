# Author: Seth Fuller
# Date: 11/27/2018
# File: Main.py

from src.Scene import Scene
from src.Thing import Thing


def main():
    scene = Scene()
    scene.set_size(800, 500)
    sprite = Thing(scene, "../assets/MaceBall.png", 20, 20)
    sprite.set_dy(5)
    sprite.set_dx(5)
    sprite.set_bounds_action(sprite.DIE)
    sprite2 = Thing(scene, "../assets/MaceBall.png", 100, 100)
    sprite2.set_bounds_action(sprite2.BOUNCE)

    scene.start()


# class CustomSprite(Thing):
#     Thing.__init__()



if __name__ == '__main__':
    while main():
        pass
