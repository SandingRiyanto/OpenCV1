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

def tampil_citra():
    img = cv2.imread('images/wayang.jpg', 0)

    # display result
    cv2.imshow('gambarnya', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# button
# tampil_citra = ttk.Button(root, text='Lihat Histogram', command=tampil_histogram)
# tampil_citra = ttk.Button(root, text='Lihat Citra', command=tampil_citra)
button1=ttk.Button(root, text="button1", command=tampil_citra)
button1.grid(row=1,column=2)

button2=ttk.Button(root, text="button2", command=tampil_histogram)
button2.grid(row=1,column=3)

# button1.pack(ipadx=5, ipady=5, expand=True)
# button2.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()
# Note: COBA BUAT 2 TOMBOL: 1) TAMPIL GAMBAR , 2) TAMPIL HISTOGRAM