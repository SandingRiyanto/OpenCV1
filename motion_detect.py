from cv2 import cv2
import numpy as np

capt = cv2.VideoCapture('video\people_walk.mp4')
ret, frame1 = capt.read()
ret, frame2 = capt.read()

while capt.isOpened():
    diff    = cv2.absdiff(frame1, frame2)
    gray    = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur    = cv2.GaussianBlur(gray, (5,5), 0)
    _,tres  = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(tres, None, iterations=3)
    kontur,_= cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for kont in kontur:
        (x,y,w,h) = cv2.boundingRect(kont)

        if cv2.contourArea(kont) < 700:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0),2)
        cv2.putText(frame1, "Status: {}".format("Movement"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
        # cv2.drawContours(frame1, kontur, -1, (0,255,0), 2)

    cv2.imshow('feed', frame1)
    frame1 = frame2
    ret, frame2 = capt.read()

    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
capt.release()