from cv2 import cv2
img = cv2.imread('images/wayang.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, biner = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)

# cv2.imshow('gambar madam lena', img)
# cv2.imshow('gambar madam lena GRAY', gray)
cv2.imshow('Citra Biner', biner)
cv2.waitKey(0)
cv2.destroyAllWindows()