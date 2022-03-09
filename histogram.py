# load and import any library
from cv2 import cv2
from matplotlib import pyplot as plt

# content
img = cv2.imread('image/sanding.jpg', 0)
plt.hist(img.ravel(), 256,[0,256])

# display result
plt.show()
cv2.imshow('gambarnya', img)
cv2.waitKey(0)
cv2.destroyAllWindows()