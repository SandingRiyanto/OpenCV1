# Import and Load Library
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from cv2 import cv2
import numpy as np
import glob
import os

# root window
root = tk.Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('Demo Aplikasi')

# Preprocessing images and convert RGB -> Grayscale
def proses_img():
    i=0
    currdir = os.getcwd()
    file_path_variable1 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    file_path_variable2 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory to Save')
    # print(file_path_variable)
    
    for img in glob.glob(file_path_variable1 + "/*.*"):
        image = cv2.imread(img)
        ImgResized = cv2.resize(image, (150, 150))

        # convert RGB to Grayscale image
        ImgGray = cv2.cvtColor(ImgResized, cv2.COLOR_BGR2GRAY)

        # save image in custom folder
        cv2.imwrite(file_path_variable2 + "/image%03i.jpg" %i, ImgGray)

        i +=1

        cv2.imshow('image', ImgGray)
        cv2.waitKey(30)

    cv2.destroyAllWindows()

# button1=ttk.Button(root, text="Pilih Folder", command=search_for_file_path).place(x=100, y=100)
button2=ttk.Button(root, text="Preprocessing!", command=proses_img).place(x=100, y=100)

root.mainloop()