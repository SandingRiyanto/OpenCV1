from cv2 import cv2
import numpy as np

capt = cv2.VideoCapture('video\people_walk.mp4')

while capt.isOpened():
    ret, frame = capt.read()
    cv2.imshow('video original', frame)

    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
capt.release()