from pynput.keyboard import Key, Controller
import numpy as np, random, cv2
from PARAMETERS import *


def move_uni(direction, last_direction):
    press = None 

    w = Key.up
    s = Key.down
    a = Key.left
    d = Key.right

    if last_direction == 0:
        if   direction == 2: press = w
        elif direction == 4: press = a
        elif direction == 6: press = d
        elif direction == 8: press = s
    

    keyboard = Controller()
    if press:
        print(press, random.random())
        keyboard.press(press)
        keyboard.release(press)


def check_direction(frame, cur_position, prev_position, last_direction):
    h, w, _ = frame.shape
    x1, y1 = cur_position
    x2, y2 = prev_position

    direction = 0 # Do Nothing

    # SENSITIVITY = 101 - SENSITIVITY

    # STATIC Directions
    # if y1 < (2*h)//5:
    #     if last_direction != 2: direction = 2 # N
    # elif y1 > (3*h)//5:
    #     if last_direction != 8: direction = 8 # S
    # else: direction = 0

    
    # DYNAMIC Directions
    if   y2 - y1 >= 100-JUMP_SENSITIVITY: direction = 2
        # if last_direction != 2: direction = 2 # N
    elif y1 - y2 >= 100-SENSITIVITY: direction = 8
        # if last_direction != 8: direction = 8 # S
    

    if   x1 - x2 >= 100-SENSITIVITY: direction = 6
        # if last_direction != 6: direction = 6 # E
    elif x2 - x1 >= 100-SENSITIVITY: direction = 4
        # if last_direction != 4: direction = 4 # W

    # return direction if direction else last_direction
    return direction


def show(frame, direction):

	RED    = (0, 0, 255)
	BLUE   = (255, 0, 0,)
	GREEN  = (0, 255, 0)
	YELLOW = (0, 255, 255)
	WHITE  = (255, 255, 255)

	h, w, _ = frame.shape
	W, H    = (w//2, h//2)

	# CENTER POINT
	frame = cv2.putText(frame, '+', (W, H), cv2.FONT_HERSHEY_SIMPLEX , 1, YELLOW, 2, cv2.LINE_AA)

	# ACTION
	action = ''
	if   direction == 2: action = 'Jump'
	elif direction == 4: action = 'Left'
	elif direction == 6: action = 'Right'
	elif direction == 8: action = 'Duck'
	frame = cv2.putText(frame, action, (7, 23), cv2.FONT_HERSHEY_SIMPLEX , 1, RED, 2, cv2.LINE_AA)

	return frame
