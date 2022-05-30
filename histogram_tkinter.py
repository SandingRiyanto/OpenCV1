# load and import any library
from cv2 import cv2
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import *

# root window
root = tk.Tk()
root.geometry('400x300')
# root.resizable(False, False)
root.title('Show Histogram of Image')

def tampil_histogram():
    # content
    img = cv2.imread('images/SR.jpg', 0)
    plt.hist(img.ravel(), 256,[0,256])

    # display result
    plt.show()

def tampil_citra():
    img = cv2.imread('images/SR.jpg', 0)

    # display result
    cv2.imshow('gambarnya', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# button
button1=ttk.Button(root, text="Show Image", command=tampil_citra).place(x=100, y=100)
button2=ttk.Button(root, text="Show Histogram", command=tampil_histogram).place(x=200, y=100)

root.mainloop()
# Note: COBA BUAT 2 TOMBOL: 1) TAMPIL GAMBAR , 2) TAMPIL HISTOGRAM --> DONE!