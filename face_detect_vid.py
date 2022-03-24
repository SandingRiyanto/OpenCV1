from cv2 import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Face Detection Video')

def face_detec_video():
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('opencv_xml/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('opencv_xml/haarcascade_eye.xml')

    # To capture video from webcam. 
    cap = cv2.VideoCapture(0)
    # To use a video file as input
    # cap = cv2.VideoCapture('filename.mp4')

    while True:
        # Read the frame
        _, img = cap.read()

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, "Status: {}".format("detected!"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),1)
        # Display
        cv2.imshow('img', img)

        # Stop if escape key is pressed
        if cv2.waitKey(10) == 27:
            break
            
    # Release the VideoCapture object
    cap.release()

# tombol
tombol = ttk.Button(root, text='Detect!', command=face_detec_video)
tombol.pack(ipadx=5, ipady=5, expand=True)
root.mainloop()