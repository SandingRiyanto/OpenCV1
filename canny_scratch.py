import matplotlib.pyplot as plt
from scipy import ndimage
from cv2 import cv2
import numpy as np

# Code by Sanding Riyanto

# ---------------------fungsi-fungsi--------------------------
# 1. sobel kernel filter
def sobel_kernel(img):
    Gx = np.array([[-1, 0, 1],
                  [-2, 0, 2],
                  [-1, 0, 1]], np.float32)

    Gy = np.array([[1, 2, 1],
                  [0, 0, 0],
                  [-1, -2, -1]], np.float32)

    Sx = ndimage.convolve(img, Gx)
    Sy = ndimage.convolve(img, Gy)

    G = np.sqrt(Sx**2 + Sy**2)
    G = G / G.max()*255

    theta = np.arctan2(Sy, Sx)

    return G, theta

# 2. non-max suppression
def non_max_suppression(img, D):
    M, N = img.shape
    Z = np.zeros((M,N), dtype=np.int32)
    angle = D * 180./np.pi
    angle[angle < 0] +=180

    for i in range(1, (M-1)):
        for j in range(1, (N-1)):
            q = 255
            r = 255

            # angle 0
            if (angle[i,j] <= 22.5) or (157.5 <= angle[i, j] <= 180):
                q = img[i, j+1]
                r = img[i, j-1]
            
            # angle 45
            if (22.5 <= angle[i, j] <= 67.5):
                q = [i+1, j-1]
                r = [i-1, j+1]

            # angle 90
            if (67.5 <= angle[i, j] <= 112.5):
                q = [i+1, j]
                r = [i-1, j]

            # angle 135
            if (112.5 <= angle[i, j] <= 157.5):
                q = [i-1, j-1]
                r = [i+1, j+1]

            if ((img[i,j] >= q).any()) and ((img[i,j] >= r).any()):
                Z[i,j] = img[i,j]
            else:
                Z[i,j] = 0
    return Z

# 3. Threshold
def threshold(img):
    highT = 200
    lowT  = 100

    M,N = img.shape
    t = np.zeros((M,N), dtype=np.int32)
    weak = np.int32(150)
    strong = np.int32(255)

    strong_i, strong_j  = np.where(img >= highT)
    zeros_i, zeros_j    = np.where(img < lowT)
    weak_i, weak_j      = np.where((img <= highT) & (img >= lowT))

    t[strong_i, strong_j] = strong
    t[weak_i, weak_j]     = weak

    return t

# 4. Hysteresis
def hysteresis(img):
    M, N = img.shape
    strong  =255
    weak    = 150

    for i in range(1, (M-1)):
        for j in range(1, (N-1)):
            if img[i,j] == weak:
                # cek semua tetangga
                if( (img[i+1, j-1] == strong) or
                    (img[i+1, j] == strong) or
                    (img[i+1, j+1] == strong) or 
                    (img[i, j-1] == strong) or
                    (img[i, j+1] == strong) or
                    (img[i-1, j-1] == strong) or
                    (img[i-1, j] == strong) or
                    (img[i-1, j+1] == strong)):
                    img[i,j] = strong
                else:
                    img[i,j] = 0
    return img

# ------------------call functions----------------------

# 0. Read Image
img1 = cv2.imread('images/sanding.jpg')
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
print("original image")
plt.imshow(img1, cmap='gray')
plt.show()

# 1. GaussianBlur -> Noise Reduction
img = img2.astype(np.float64)
img_blur = cv2.GaussianBlur(img, (5,5), 0)
print("hasil gaussian blur filter 5x5")
plt.imshow(img_blur, cmap='gray')
plt.show()

# 2. Calculate Gradien Magnitude
img_sobel, arah = sobel_kernel(img_blur)
print("hasil dari gradien magnitude")
plt.imshow(img_sobel, cmap='gray')
plt.show()

# 3. Non-Maximum Suppression
non_max_s = non_max_suppression(img_sobel, arah)
print("hasil dari non-max-suppression")
plt.imshow(non_max_s, cmap='gray')
plt.show()

# 4. Double Threshold
th = threshold(non_max_s)
print("hasil dari threshold")
plt.imshow(th, cmap='gray')
plt.show()

# 5. Hysteresis
tepi = hysteresis(th)
print("hasil dari akhir Canny-Scratch")
plt.imshow(tepi, cmap='gray')
plt.show()