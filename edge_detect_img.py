from cv2 import cv2
import numpy as np

# akuisisi citra
image = cv2.imread('images/rizka.jpg')
ImgResized = cv2.resize(image, (300, 400))
abu     = cv2.cvtColor(ImgResized, cv2.COLOR_BGR2GRAY)
tepi    = cv2.Canny(abu, 100, 200)
kontur, hirarki = cv2.findContours(tepi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# hitung objek citra
jumlah = str(len(kontur))
print("jumlah objek: ", jumlah)

hasil_kontur = cv2.drawContours(image, kontur, -1, (0,255,0), 2) #format warna: Blu-Green-Red | ketebalan

# cv2.imshow("hasil kontur", hasil_kontur)
cv2.imshow("Canny", tepi)
cv2.imwrite('images/saved.jpg', tepi)

cv2.waitKey(0)
cv2.destroyAllWindows()