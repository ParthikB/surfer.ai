import cv2

CAM_IDX = 1

RED    = (0, 0, 255)
BLUE   = (255, 0, 0,)
GREEN  = (0, 255, 0)
YELLOW = (0, 255, 255)
ALPHA  = 0.25
FREE_RAD_FACTOR = 7


def show_direction(frame, coords):
    x, y = coords

    h, w, _ = frame.shape

    W, H       = (w//2, h//2)
    FREE_RAD   = h//FREE_RAD_FACTOR
    rr         = W + FREE_RAD
    lr         = W - FREE_RAD
    ur         = H - FREE_RAD
    dr         = H + FREE_RAD

    if   x <= lr and y <= ur: return 1 # NW
    elif x <= rr and y <= ur: return 2 # N
    elif x <= w  and y <= ur: return 3 # NE
    elif x <= lr and y <= dr: return 4 # W
    elif x <= rr and y <= dr: return 5 # Null
    elif x <= w  and y <= dr: return 6 # E
    elif x <= lr and y <= h:  return 7 # SW
    elif x <= rr and y <= h:  return 8 # S
    elif x <= w  and y <= h:  return 9 # SE
    else: return 5 # Null


def draw_point(frame, coords, radius=2, color=(255, 255, 255)):
    cv2.circle(frame, coords, radius, color, -1)

def draw_rect(frame, start_coord, end_coord, color=(255, 255, 255)):
    cv2.rectangle(frame, start_coord, end_coord, color, -1)     

def show(frame, direction):

    overlay = frame.copy()

    h, w, _ = frame.shape

    W, H       = (w//2, h//2)
    FREE_RAD   = h//FREE_RAD_FACTOR
    RR         = W + FREE_RAD
    LR         = W - FREE_RAD
    UR         = H - FREE_RAD
    DR         = H + FREE_RAD

    TL = (LR, UR)
    TR = (RR, UR)
    BL = (LR, DR)
    BR = (RR, DR)

    area_c = [BLUE] *9
    area_c[direction-1] = GREEN

    # CENTER POINT
    draw_point(frame, (W, H), color=YELLOW)
    # cv2.circle(frame, (W, H), 2, (0, 255, 255), -1)

    # FREE AREA
    cv2.circle(frame, (W, H), FREE_RAD, (0, 255, 255))

    draw_point(frame, TL, color=GREEN) # top left
    draw_point(frame, TR, color=GREEN) # top right
    draw_point(frame, BL, color=GREEN) # bottom left
    draw_point(frame, BR, color=GREEN) # bottom right

    draw_rect(frame, (0, 0), TL,        color=area_c[0])
    draw_rect(frame, (LR, 0), TR,       color=area_c[1])
    draw_rect(frame, (RR, 0), (w, UR),  color=area_c[2])

    draw_rect(frame, (0, UR), (LR, DR), color=area_c[3])
    draw_rect(frame, (RR, UR), (w, DR), color=area_c[5])


    draw_rect(frame, (0, DR), (LR, h),  color=area_c[6])
    draw_rect(frame, (LR, DR), (RR, h), color=area_c[7])
    draw_rect(frame, (RR, DR), (w, h),  color=area_c[8])


    return cv2.addWeighted(overlay, 1-ALPHA, frame, ALPHA, 0)
