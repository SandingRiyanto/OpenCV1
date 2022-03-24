import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Canny Edge Detection')

# fungsi
def edge_detect():
    from cv2 import cv2
    import numpy as np

    # akuisisi citra
    fileku = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=(("JPG file", "*.jpg"), ("PNG file", "*.png"), ("All files", "*.*")))
    img = cv2.imread(fileku)
    # img = cv2.imread('images/wayang.jpg') # masih statis -> pakai open file dialog tkinter!
    abu     = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    tepi    = cv2.Canny(abu, 100, 200)
    kontur, hirarki = cv2.findContours(tepi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # hitung objek citra
    # jumlah = str(len(kontur))
    # print("jumlah objek: ", jumlah)

    hasil_kontur = cv2.drawContours(img, kontur, -1, (0,255,0), 2) #format warna: Blu-Green-Red | ketebalan

    # cv2.imshow("hasil kontur", hasil_kontur)
    cv2.imshow("Canny", tepi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# exit button
tampil_citra = ttk.Button(root, text='Tampilkan', command=edge_detect)

tampil_citra.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()