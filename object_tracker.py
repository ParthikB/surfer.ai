from pyimagesearch.centroidtracker_mine import CentroidTracker
from imutils.video import VideoStream
import numpy as np
import cv2
import argparse
import imutils
import time
import game_utils
from __helper__ import *



ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True, help="Path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True, help="Path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.5, help="Minimum probability to filter weak detections")
args = vars(ap.parse_args())


ct = CentroidTracker()
(H, W) = (None, None)

print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

print("[INFO] starting video stream...")
vs = VideoStream(src=CAM_IDX).start()
time.sleep(2.0)

position = []
last_position = (0, 0)
direction = 0

q = -1

while True:
    frame = vs.read()
    q += 1

    frame = cv2.flip(frame, 1)
    frame = imutils.resize(frame, width=400)

    if W is None or H is None:
        H, W = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 1.0, (W, H), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()
    rects = []

    cur_position = None
    for i in range(0, detections.shape[2]):

        if detections[0, 0, i, 2] > args['confidence']:
            box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
            rects.append(box.astype("int"))

            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

            diagnol = pow((startX-endX)**2 + (startY-endY)**2, 0.5)
            area    = pow(diagnol, 2)
            cur_position = ((startX+endX)//2, (startY+endY)//2)
            
# ####
    if cur_position: # If Something is detected
        if q % CHECK_AFTER_EVERY == 0:
            last_direction = direction
            direction = check_direction(frame, cur_position, last_position, direction)

            print(direction, last_direction)
            game_utils.move_uni(direction, last_direction)
            last_position = cur_position
# ####
    
    objects = ct.update(rects)
    # print(len(objects), objects)

    for (objectID, centroid) in objects.items():
        text = "ID {}".format(objectID)
        cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)
# ####
    frame = show(frame, direction, text_only=True)
# ####


    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cv2.destroyAllWindows()
vs.stop()


# 