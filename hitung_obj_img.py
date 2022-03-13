from cv2 import cv2
import numpy as np

# rescale frame (bikin default 75)
def rescale_frame(frame, percent=75):
    width   =int(frame.shape[1]*percent/100)
    height  =int(frame.shape[0]*percent/100)
    dim     =(width,height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

image = cv2.imread('images/bentuk.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# image   = rescale_frame(frame, percent=100)
abu     = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
tepi    = cv2.Canny(abu, 100, 200)
kontur, hirarki = cv2.findContours(tepi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
jumlah = str(len(kontur))
print("jumlah objek: ", jumlah)

hasil_kontur = cv2.drawContours(image, kontur, -1, (0,255,0), 2)

# cv2.imshow("hasil kontur", hasil_kontur)
cv2.imshow("Canny", tepi)
cv2.waitKey(0)
cv2.destroyAllWindows()