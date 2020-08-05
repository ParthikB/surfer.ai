import cv2

CAM_IDX 		  = 0
SENSITIVITY 	  = 25 # 0-100
CHECK_AFTER_EVERY = 3  # Min 1
ALPHA  			  = 0.25 


def draw_point(frame, coords, radius=2, color=(255, 255, 255)):
    cv2.circle(frame, coords, radius, color, -1)

def draw_rect(frame, start_coord, end_coord, color=(255, 255, 255)):
    cv2.rectangle(frame, start_coord, end_coord, color, -1)    


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
    if   y2 - y1 >= SENSITIVITY: direction = 2
        # if last_direction != 2: direction = 2 # N
    elif y1 - y2 >= SENSITIVITY: direction = 8
        # if last_direction != 8: direction = 8 # S
    

    if   x1 - x2 >= SENSITIVITY: direction = 6
        # if last_direction != 6: direction = 6 # E
    elif x2 - x1 >= SENSITIVITY: direction = 4
        # if last_direction != 4: direction = 4 # W

    # return direction if direction else last_direction
    return direction


 

def show(frame, direction, text_only=False):

	RED    = (0, 0, 255)
	BLUE   = (255, 0, 0,)
	GREEN  = (0, 255, 0)
	YELLOW = (0, 255, 255)
	WHITE  = (255, 255, 255)

	overlay = frame.copy()
	h, w, _ = frame.shape
	W, H    = (w//2, h//2)

	# CENTER POINT
	overlay = cv2.putText(overlay, '+', (W, H), cv2.FONT_HERSHEY_SIMPLEX , 1, YELLOW, 2, cv2.LINE_AA)

	# ACTION
	action = ''
	if   direction == 2: action = 'Jump'
	elif direction == 4: action = 'Left'
	elif direction == 6: action = 'Right'
	elif direction == 8: action = 'Duck'
	overlay = cv2.putText(overlay, action, (7, 23), cv2.FONT_HERSHEY_SIMPLEX , 1, WHITE, 2, cv2.LINE_AA)

	if not text_only:
		area_c = [BLUE] *2
		if   direction == 2: area_c[0] = GREEN
		elif direction == 8: area_c[1] = GREEN

		# JUMP AREA
		draw_rect(frame, (0, 0), (w, (2*h)//5), color=area_c[0])

		# DUCK AREA
		draw_rect(frame, (0, (3*h)//5), (w, h), color=area_c[1])

	return cv2.addWeighted(overlay, 1-ALPHA, frame, ALPHA, 0)
