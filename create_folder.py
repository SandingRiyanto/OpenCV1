from cv2 import cv2
import os

if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")

    os.makedirs("data/train/satu")
    os.makedirs("data/train/dua")
    os.makedirs("data/train/tiga")

    os.makedirs("data/test/satu")
    os.makedirs("data/test/dua")
    os.makedirs("data/test/tiga")