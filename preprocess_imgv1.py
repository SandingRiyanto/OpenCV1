# Import and Load Library
import numpy as np
from cv2 import cv2
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import os
import glob

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Demo Aplikasi')

# fungsi untuk akuisisi citra-convert-save dengan loop
def proses_img():

    path = "images\*.*"
    for bb, file in enumerate (glob.glob(path)):
        image_read = cv2.imread(file)
        # konversi rgb -> gray -> biner
        gray = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
        ret, biner = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
        
        # cv2.imshow('Color image', biner)
        # writing the images in a folder output_images
        cv2.imwrite('images\simpan\gambar{}.png'.format(bb), biner)
        print("loading....")
        k = cv2.waitKey(1000)
        cv2.destroyAllWindows()

# tombol
tombol1 = ttk.Button(root, text='Proses!', command=proses_img)
tombol1.pack(ipadx=5, ipady=5, expand=True)
root.mainloop()