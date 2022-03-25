import numpy as np
from cv2 import cv2
# from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import os

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Demo Aplikasi')

def face_detect_img():

    # diambil dari opencv github
    face_cascade = cv2.CascadeClassifier('opencv_xml/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('opencv_xml/haarcascade_eye.xml')

    fileku = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=(("JPG file", "*.jpg"), ("PNG file", "*.png"), ("All files", "*.*")))
    img = cv2.imread(fileku)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 3)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray    = gray[y:y+h, x:x+w]
        roi_color   = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('Display Images',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

tombol1 = ttk.Button(root, text='Detect!', command=face_detect_img)
tombol1.pack(ipadx=5, ipady=5, expand=True)
root.mainloop()