from tkinter import *
from tkinter import filedialog
import os
# from PIL import Image, ImageTk
from cv2 import cv2
import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Demo Aplikasi')

# fungsi untuk load image file dan menampilkannya dengan lib openCV
def tampil_img():
    fileku = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=(("JPG file", "*.jpg"), ("PNG file", "*.png"), ("All files", "*.*")))
    # img = Image.open(fileku)
    img = cv2.imread(fileku)
    # DI SINI TINGGAL DIMASUKAN CODE UNTUK OLAH IMAGE/VIDEO -> DETEKSI TEPI ATAU YG LAINNYA
    cv2.imshow("gambar", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # print(img)

# tombol untuk show path image
tampil_citra = ttk.Button(root, text='Open Image File', command=tampil_img)

tampil_citra.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()