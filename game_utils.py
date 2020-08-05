from pynput.keyboard import Key, Controller
import numpy as np
import random


def move_uni(direction, last_direction):
    # if direction == 0: return False # Do Nothing
    press = None 

    w = Key.up
    s = Key.down
    a = Key.left
    d = Key.right

    # if   direction == 2 and last_direction != 2 : press = w
    # elif direction == 4 and last_direction != 4 : press = a
    # elif direction == 6 and last_direction != 6 : press = d
    # elif direction == 8 and last_direction != 8 : press = s

    if last_direction == 0:
        if   direction == 2: press = w
        elif direction == 4: press = a
        elif direction == 6: press = d
        elif direction == 8: press = s
    

    keyboard = Controller()
    # keyboard.type(press)
    if press:
        print(press, random.random())
        keyboard.press(press)
        keyboard.release(press)