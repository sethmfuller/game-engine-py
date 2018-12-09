# Game Engine - Python

## Overview

This engine is built upon Pygame.

## Main Constructs

### Scene

In general, every game will have one Scene instantiation. The Scene is where sprites will be placed and the main game loop occurs.
These are the basic features and properties that you can modify for the Scene:

- Screen
- size
- color
- [`update()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Scene.py#L20)
- [`add_sprite()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Scene.py#L39): Adds a sprite to the scene so that it can be updated every iteration of the game loop
- [`start()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Scene.py#L43): Starts the game loop

### Thing

The Thing class is essentially a subclass of the `pygame.sprite.Sprite`. It supports these basic features and properties that you can modify:

- x, y
- dx, dy
- visible
- Bounding Actions: `LEAVE`, `SKID`, `DIE`, `BOUNCE`, `STOP`
- [`check_bounds()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Thing.py#L52)
- [`check_keys()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Thing.py#L81)
- [`update()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Thing.py#L33)
- [`set_position()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Thing.py#L101)
- [`set_x()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Thing.py#L105)
- [`set_y()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Thing.py#L108)
- [`change_x_by()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Thing.py#L111)
- [`change_y_by()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Thing.py#L114)
- [`set_dx()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Thing.py#L117)
- [`set_dy()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Thing.py#L120)
- [`change_dx_by()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Thing.py#L123)
- [`change_dy_by()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Thing.py#L126)
- [`flip()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Thing.py#L133)
- [`scale()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Thing.py#L136)
- [`rotate()`](https://github.com/sethmfuller/game-engine-py/blob/master/src/Thing.py#L139)
