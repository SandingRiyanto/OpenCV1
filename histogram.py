# load and import any library
from cv2 import cv2
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Show Histogram of Image')

def tampil_histogram():
    # content
    img = cv2.imread('images/wayang.jpg', 0)
    plt.hist(img.ravel(), 256,[0,256])

    # display result
    plt.show()
    cv2.imshow('gambarnya', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# button
tampil_citra = ttk.Button(root, text='Lihat Histogram', command=tampil_histogram)
# tampil_citra = ttk.Button(root, text='Lihat Histogram', command=tampil_histogram)

tampil_citra.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()