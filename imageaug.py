import imgaug.augmenters as iaa
from tkinter import filedialog
import cv2
import glob
import os
from tkinter import ttk
import tkinter as tk

# 1. Load Dataset

root = tk.Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('Demo Aplikasi')

currdir = os.getcwd()
file_path_variable1 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
file_path_variable2 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory to Save')

images = []
images_path = glob.glob(file_path_variable1 + "/*.jpg")
for img_path in images_path:
    img = cv2.imread(img_path)
    images.append(img)

# 2. Image Augmentation
augmentation = iaa.Sequential([
    # 1. Flip
    # iaa.Fliplr(1.0),

    # 2. Affine
    iaa.Affine(
        scale={"x": (0.8, 1.2), "y": (0.8, 1.2)})
        # translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)},
])

# 3. Show Images
augmented_images = augmentation(images=images)
# print(augmented_images)
i=0
for img in augmented_images:
    # gambar = cv2.imread(img)
    cv2.imshow("Image", img)
    
    cv2.imwrite(file_path_variable2 + "/image%03i.jpg" %i, img)
    i +=1
    print(i)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()