from pynput.keyboard import Key, Controller
import numpy as np


# def square(x):
#     return np.sqare(x)


# def euclidian_distance(old_coods, new_coords):
#     x1, y1 = old_coords
#     x, y   = new_coords

#     np.sqrt(square(y1-x1) + square(y-x)) = distance

    
# coords = [123, 456.8]

def move(coords):
    if len(coords) != 2: return None

    old_coords, new_coords = coords
    p, q = old_coords
    x, y = new_coords

    if x-p > 0:   x_axis = 'a'
    elif x-p < 0: x_axis = 'd'
    else:         x_axis = '-'

    if y-q > 0:   y_axis = 's'    
    elif y-q < 0: y_axis = 'w'
    else:         y_axis = '-'

    print(x_axis, y_axis)


    keyboard = Controller()
# def player_at_coords(coords):
    keyboard.type((x_axis, y_axis))


def move_uni(direction):
    
    if direction == 5: return False

    press = 'z' #dummy

    if   direction == 1: press = 'wa'
    elif direction == 2: press = 'w'
    elif direction == 3: press = 'wd'
    elif direction == 4: press = 'a'
    elif direction == 6: press = 'd'
    elif direction == 7: press = 'sa'
    elif direction == 8: press = 's'
    elif direction == 8: press = 'sd'

    print(press)

    keyboard = Controller()
    keyboard.type(press)



def move_uni(direction):
    
    if direction == 0: return False # Do Nothing

    press = 'z' # Dummy

    w = Key.up
    s = Key.down
    a = Key.left
    d = Key.right

    

    # if   direction == 1: press = 'wa' 
    if   direction == 2: press = w
    # elif direction == 3: press = 'wd'
    elif direction == 4: press = a
    elif direction == 6: press = d
    # elif direction == 7: press = 'sa'
    elif direction == 8: press = s
    # elif direction == 9: press = 'sd'

    import random
    print(press, random.random())

    keyboard = Controller()
    # keyboard.type(press)
    keyboard.press(press)
    keyboard.release(press)