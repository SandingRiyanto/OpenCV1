from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk
from cv2 import cv2
import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Canny Edge Detection')

def tampil_img():
    fileku = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=(("JPG file", "*.jpg"), ("PNG file", "*.png"), ("All files", "*.*")))
    img = Image.open(fileku)
    # cv2.imshow("tampil gambar", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print(img)

tampil_citra = ttk.Button(root, text='Tampilkan', command=tampil_img)

tampil_citra.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()