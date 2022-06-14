import time
import cv2
import matplotlib.pylab as plt
from imutils import resize
print(cv2.__version__)

# multi_tracker = cv2.MultiTracker_create()
multi_tracker = cv2.Tracker_create(tracker_type)

car_bbox = (141,175,45,29)
car2_bbox = (295,170,55,39)
bboxes = [car_bbox, car2_bbox]
colors = [(0, 255, 255), (255, 255, 0)]

vs = cv2.VideoCapture('video/car_walk.mp4')
_, frame = vs.read()
frame = resize(frame, width=500)
for bbox in bboxes:
    multi_tracker.add(cv2.TrackerCSRT_create(), frame, bbox)

j = 0
while True:
    vs.set(cv2.CAP_PROP_POS_MSEC,(j*300)) # 1 sec read 3 frames
    _, frame = vs.read()

    if frame is None:
        break

frame = resize(frame, width=500)
success, boxes = multi_tracker.update(frame)
if success:
    for i, box in enumerate(boxes):
        p1 = (int(box[0]), int(box[1]))
        p2 = (int(box[0] + box[2]), int(box[1] + box[3]))
        cv2.rectangle(frame, p1, p2, colors[i], 2, 1)
    j += 1