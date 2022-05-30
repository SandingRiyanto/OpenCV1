from cv2 import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/SR.jpg')
ImgResized = cv2.resize(img, (400, 580))
gray = cv2.cvtColor(ImgResized, cv2.COLOR_BGR2GRAY)
ret, biner = cv2.threshold(gray, 82, 255, cv2.THRESH_BINARY)

# cv2.imshow('gambar madam lena', img)
# cv2.imshow('gambar madam lena GRAY', gray)
# cv2.imshow('Citra Biner', biner)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


plt.imshow(biner)
plt.show()