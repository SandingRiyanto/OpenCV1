from cv2 import cv2

capture = cv2.VideoCapture(0)

while True:
    #!openkamera
    _, frame = capture.read()

    x1 = 400
    y1 = 10

    x2 = 610
    y2 = 250

    # buat garis kotak (biru)
    cv2.rectangle(frame, (x1-1,y1-1), (x2+1,y2+1), (255,0,0), 1)
    roi = frame[y1:y2, x1:x2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY) #grayscale image of roi
    _, roi = cv2.threshold(roi, 50, 255, cv2.THRESH_BINARY)

    # display
    cv2.imshow('frame', frame)
    cv2.imshow('ROI', roi)

    # ketika pencet 'c' maka akan ter-capture dan 'esc' akan ter-close
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:
        break
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite('image/saved.jpg', roi)

capture.release()
cv2.destroyAllWindows()